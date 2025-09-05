# Time Tracking Assistant

**AI‑powered time tracking that highlights _value_, not just hours.**  
Runs securely, observes opt‑in work signals, and drafts concise “value entries” you can confirm or quick‑add at day’s end.

<p align="left">
  <a href="https://github.com/jrkropp/time-tracking-assistant">
    <img alt="Status" src="https://img.shields.io/badge/status-early%20alpha-FFD166.svg">
  </a>
  <img alt="Focus" src="https://img.shields.io/badge/focus-value--first-blueviolet">
  <img alt="AI Optional" src="https://img.shields.io/badge/AI-BYOK%20optional-06B6D4">
  <img alt="Privacy" src="https://img.shields.io/badge/privacy-local--first-10B981">
  <img alt="License" src="https://img.shields.io/badge/license-TBD-lightgrey">
</p>

---

## Table of Contents

- [What the app does](#what-the-app-does)
- [How this app is different — the value‑first shift](#how-this-app-is-different--the-valuefirst-shift)
- [Who this app is for / not for](#who-this-app-is-for)
- [Day in the life](#day-in-the-life)
- [Core concepts](#core-concepts)
- [Examples of value‑first entries](#examples-of-valuefirst-entries)
- [Privacy & security](#privacy--security-principles)
- [Roadmap](#roadmap)
- [Status](#status)
- [License & contributing](#license--contributing)

---

## What the app does

- **Auto‑suggests value entries.** As you work, the app quietly reads the **signals you choose to enable** (calendar events, email threads, documents, commits—and in desktop mode, active apps/files). From those, it proposes **draft entries** that describe the _outcome_ you delivered.
- **End‑of‑day review.** Instead of babysitting a stopwatch, you get a clean **queue** of suggestions. Skim, tweak, **confirm** the ones that reflect real value, and **discard** the rest.
- **Value‑first summaries.** Entries are short, client‑safe statements in past tense (≤45 words) that name the beneficiary and the impact (e.g., _“Restored Finance VPN access; validated with test sign‑in; reduced downtime risk.”_). Duration is captured, but secondary.
- **Quick Add.** Add your own value moments in seconds—great for ad‑hoc wins that signals might miss.
- **Selective publish.** Only confirmed entries are pushed to your time/ticketing/reporting systems.

> **TL;DR flow:** _Capture → Review → Publish_ — with value first, time second.

---

## How this app is different — the value‑first shift

Most trackers are **time‑first**:  
> _“I spent 3.5 hours on project X.”_

This app is **value‑first**:  
> _“Restored Finance team’s VPN access, reducing downtime risk.”_

That’s a **subtle but powerful mindset shift**: from _accounting for time spent_ → to _accounting for value delivered_.  
Time is a cost; **value is the outcome**. When you optimize for outcomes:

### Two key effects

1. **Unlimited upside.**  
   Your daily output isn’t capped at 100% of a clock. One high‑leverage fix can produce **more than 100% value**—for example, minutes of work that unlock hours for a team, reduce risk, or prevent outages.

2. **Accountability through visibility.**  
   Conversely, if you aren’t providing actual value, the tool will make that visible. It won’t generate drafts out of thin air—if no meaningful outcomes occurred, your queue will be empty. This keeps you honest with yourself and transparent with others.

---

## Who this app is for

- **Consultants / MSPs / IT / Engineering** who need client‑safe, outcome‑led notes.  
- **Leads & ICs** who want weekly updates that show results, not just effort.  
- **Anyone** who prefers a single end‑of‑day review instead of reconstructing the day from memory.

### Who this app is _not_ for

- If you just want to **track time spent** with a start/stop timer, a tool like **Toggl** or **Harvest** will suit you better.  
- If you need **payroll‑grade timesheets** without narrative value, traditional timesheet systems are a better fit.

_This app is for people who want software that is **constantly hunting for the value they created** and presenting it back for review—so the story of the day reflects outcomes, not just hours._

---

## Day in the life

1. **Work normally.** Enable only the signals you’re comfortable with (e.g., calendar + email + documents). The app quietly proposes drafts with sensible durations.  
2. **Review once.** At day’s end, open **Today**, skim the drafts, tighten wording if needed, **confirm** the true wins, and **discard** the rest.  
3. **Publish.** Send the confirmed entries to your time/ticketing/reporting systems. Start tomorrow with a clear queue.

> You stay in control: nothing is published until you confirm it.

---

## Core concepts

- **Value Entry** — a 1–2 sentence, plain‑language summary (≤45 words) in past tense that names the **beneficiary** and the **outcome/impact**.  
  _Example:_ “Finance — **restored** VPN access after policy drift; **validated** with test sign‑in and device health; **reduced** downtime risk.”

- **Signals** — lightweight breadcrumbs (calendar invites, email threads, edited docs, commits, app/file focus) used to **propose** drafts. You choose which signals are enabled and what is shared.

- **Statuses** — `Draft → Confirmed → Published` (or `Discarded`). Drafts can be edited; published entries are read‑only.

- **Quick Add** — capture wins in seconds when inspiration strikes.

---

## Examples of value‑first entries

- “HR — **standardized** onboarding checklist; **reduced** setup time ~30%; **validated** with pilot for two new hires.”  
- “Client Ops — **remediated** mailbox send failures by correcting SPF/DMARC; **confirmed** with test sends + Postmaster diagnostics.”  
- “Product — **clarified** SSO rollout scope; **aligned** Security + IT on phased plan; **unblocked** sprint delivery.”

---

## Privacy & security (principles)

- **User control first.** You decide which signals are enabled and what gets published.  
- **AI optional (BYOK).** Bring your own key if you want AI assists, or run with AI off for a local‑only experience.  
- **Local‑first mindset.** Designed to run securely on your machine; no raw artifacts are shared without your say‑so.  
- **Redaction by default.** PII and sensitive identifiers can be scrubbed from AI prompts and published entries.

---

## Roadmap

### Phase 1 — **Quick Add MVP** ✅ (current)
- Manually type or paste what you did (task, email, resolution notes).  
- Saved as a **draft entry** in your queue.  
- **Edit, tag, and categorize** entries.  
- End‑of‑day: confirm or discard.

_This phase proves the **value‑entry workflow** (capture → edit → confirm) before integrations are implemented._


---

## Status

Early days. The goal is to **reduce friction** while **raising the quality** of time notes—centered on _value delivered_.  
This app isn’t about counting hours. It’s about **surfacing impact**, **keeping you accountable**, and **making the invisible value of your work visible**.

---

## License & contributing

**License:** TBD  
**Contributing:** If you want to help shape the value‑first approach—use cases, workflows, or examples of great entries—please open an issue or discussion.

---

> _Have a great example of a value‑first entry? Add it to an issue—real examples help sharpen the product._
