# Design Documentation
## What is this document?

This is a design record that captures the **why** behind a significant architecture decision in the OpenAI Responses manifold. It is not a how-to guide and does not explain implementation details or usage. The goal is to document context, decision, alternatives, trade-offs, and acceptance criteria so future contributors understand the rationale.

How this document is structured:

* **Questions** frame the decision and its context.
* **Answers** describe the intent and rationale, not implementation steps.
* **Scope** is limited to design motivations and consequences.

---

# Design Decisions

---

## 1) What problem are we solving and what is the core user loop?

**Answer**  
We help people produce concise, value‑first daily entries from their work “signals” (calendar, email, docs, commits). The loop is:

1. Ingest signals.
2. Generate short draft entries (≤45 words; beneficiary + outcome).
3. User reviews, edits, and confirms.
4. Publish or export; nothing auto‑publishes.

**Implications**
- We need reliable, server‑side ingestion and a simple UI for review and confirmation.
- OS‑level monitoring is *not required* to deliver the core loop.

---

## 2) Should v1 be a web app or a desktop app?

**Decision**  
**Web app (PWA) first**, with the option to add:
- a **browser extension** (quick capture, page URL/title, hotkey while the browser is focused), and
- a **desktop companion (later, optional)** for native signals (frontmost app, file path) and a global hotkey.

**Why (simple logic)**
- The **web** removes install friction, works everywhere, and still delivers the full core loop.
- The few things **desktop** adds (global hotkey, OS context, strong offline) are valuable but *not prerequisites*.
- We can meet “quick add” needs with a **browser extension** before investing in a full desktop agent.

**Alternatives considered**
- Desktop‑first (Electron/Tauri/Native): Highest ops and security surface; slows pilots.
- Hybrid at v1 (web + desktop): Doubles QA and packaging before we’ve proven value.

**Trade‑offs (plain language)**
- **Web pros:** zero‑install, fast iteration, simpler auth/security, broad reach.
- **Web cons:** no true global hotkey; limited background abilities in the browser.
- **Desktop pros:** OS‑level hotkey and context; robust offline/background.
- **Desktop cons:** packaging/signing/updates; larger security surface; higher support cost.

---

## 3) If the browser isn’t open, how does monitoring work?

**Answer**  
**Monitoring runs on the backend, not in the browser.**  
- Microsoft 365: Graph **change notifications** (webhooks) or **Event Hubs** delivery; **delta queries** for catch‑up.
- GitHub: **Webhooks** (preferred) with polling as a fallback.
- Workers normalize events → redact → generate drafts → store provenance.

**Implications**
- The UI can be closed; ingestion still runs.
- The PWA is a thin client for review, edit, and confirm.

---

## 4) How do we deploy, and where do secrets live?

**Decision**
- Support **two modes**:
  1) **Cloud / self‑hosted**: containers for API, worker; managed Postgres; secret manager; HTTPS ingress for webhooks.
  2) **Local single‑user** (Docker Compose): same components locally; polling or a tunnel for webhooks (for demos/dev).
- **Secrets** (SSO client secret, API keys, webhook secrets, DB creds, VAPID keys) are kept in a secret manager and **injected via environment variables** at runtime. They are never committed to the repo and never logged.

**Why**
- Keeps the PWA stateless and easy to ship.
- Keeps sensitive material out of source control and in auditable stores.

---

## 5) What could go wrong, and how do we mitigate it?

**Answer**
- **Local cache eviction (PWA)** → Keep the client stateless; server is the source of truth; explicit resync.
- **Webhook outages / rate limits** → Use retry queues, exponential backoff, delta queries for catch‑up; idempotent upserts keyed by subscription/resource.
- **Secrets leakage risk** → Use a secret manager; scoped env injection; rotate keys; never log secrets.
- **Early demand for hotkey/URL capture** → Ship **browser extension** first (smaller surface than desktop).

---

## 6) When do we revisit the desktop decision?

**Answer**
Add a **browser extension** when ≥25% of active users adopt quick‑add workflows that are hindered by the lack of a hotkey.  
Build a **desktop companion** when A/B tests show native signals increase draft acceptance or reduce editing time by **≥10%**, or when enterprise pilots require offline‑first with endpoint‑only processing.

---

## 7) High‑level architecture (for context)

**Answer**
- **PWA (React/TS)** → Auth, Today queue, Quick Add, edit/confirm.
- **API** → AuthN/AuthZ, drafts, entries, notification orchestration.
- **Worker** → Connector ingestion (Graph/GitHub), redaction, draft generation, outbound publishing.
- **Connectors** → Microsoft Graph (webhooks/Event Hubs + delta), GitHub webhooks (poll fallback).
- **Storage** → Postgres (entries, provenance, cursors), object store if needed; Redis for queues.
- **Secrets** → Secret manager; env injection at runtime.
