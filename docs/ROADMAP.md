# Technical Roadmap — Dan Melendez AI Consultancy Distribution Engine
**Version:** 1.1 | **Date:** 2026-05-01 | **Deadline:** End of May 2026

Status legend: ✅ Done · 🔄 In progress · ⏳ Queued · 🔮 V3 (post-May)

---

## Confirmed Decisions

| Topic | Decision |
|-------|----------|
| Analytics | GA4 (free) |
| Lead store | Google Sheets → custom tool later |
| Languages | Spanish + English both |
| Funnel | Full diagnosis free → "Want more?" → $49 onboarding plan + call |
| Substack CTA | Soft: "Let's keep in touch — I'm sure you'll find something valuable" |
| Assessment URL | `https://adv-1-lac.vercel.app/` |
| Landing page URL | `https://beamish-starlight-f50127.netlify.app/` |
| Stack commitment | None — Vercel + Netlify are PoC only, all modules are portable |

---

## Phase 1 — Foundation (Week 1) ✅ COMPLETE

**Tracer bullet goal:** Prove both products are live, connected, and findable.

| Task | Module | Status | Notes |
|------|--------|--------|-------|
| Fix OpenAI model name (gpt-4o-mini) | M1 | ✅ | Was gpt-5-mini — invalid |
| Simplify response parser | M1 | ✅ | Removed OpenRouter-era extract_text() |
| Make MODEL_NAME env-var driven | M1 | ✅ | Defaults to gpt-4o-mini |
| Add meta description + OG + Twitter tags | M2 | ✅ | |
| Fix nav Substack link | M2 | ✅ | Was plain text span |
| Add assessment CTA to landing page | M2 | ✅ | Links to adv-1-lac.vercel.app |
| Add _redirects | M2 | ✅ | 404 fallback |
| PDR, Governance, Roadmap v1.0 | Docs | ✅ | |
| PDR, Roadmap v1.1 (all decisions locked) | Docs | ✅ | This update |

**Manual action still required:** Set `OPENAI_API_KEY` in the API host project environment variables.

---

## Phase 2 — Conversational UI + Instrumentation (Week 2) ⏳

**Tracer bullet goal:** One question delivered as a chat message, answer written to Google Sheets in real time.

### M1 — Conversational UI upgrade

| Task | Priority | Est. |
|------|----------|------|
| Redesign assessment as chat UI (message bubbles, typing indicator, not a form) | High | 2h |
| Persist each answer to `/api/events` as user answers — not on submit | High | 1h |
| Store contact info before question 1 starts | High | 30m |
| Add language toggle (Spanish / English) — all strings externalized | Medium | 1h |
| Add UTM source capture on session start | Medium | 30m |

**Chat flow spec:**
```
Agent: "Hi — I'm here to assess your company's AI readiness. What's your name?"
User:  "Sarah"
Agent: "And your email so I can send you the results?"
User:  "sarah@company.com"
Agent: "Question 1 of 10: Does your company have a documented data strategy?"
       [A] No documented strategy
       [B] Informal understanding
       [C] Formal, documented strategy
```

### M3 — Analytics + Lead Capture

| Task | Priority | Est. |
|------|----------|------|
| Add GA4 script + cookie consent banner to landing page | High | 45m |
| Add GA4 to assessment, track `assessment_start`, `email_captured`, `assessment_complete` | High | 1h |
| Create `/api/events` endpoint → append row to Google Sheets via Sheets API | High | 1h |
| Set up Google Sheet: Leads tab (schema from PDR §3 M1) | High | 30m |

**New env vars for Phase 2:**
```
GOOGLE_SHEETS_ID=
GOOGLE_SERVICE_ACCOUNT_JSON=
GA4_MEASUREMENT_ID=
```

---

## Phase 3 — Monetization (Week 3) ⏳

**Tracer bullet goal:** One test payment of $49 triggers a Stripe webhook that writes "paid" to the lead's Google Sheets row and returns the onboarding plan in-browser.

### M4 — $49 Paywall

| Task | Priority | Est. |
|------|----------|------|
| Set up Stripe product: $49 "AI Readiness Onboarding Plan + Call" | High | 30m |
| Add `/api/checkout` → creates Stripe Checkout session | High | 1h |
| Add `/api/webhook` → handles payment success: update Sheets + return plan | High | 1h |
| Post-diagnosis CTA: "Want more?" button → Stripe Checkout | High | 45m |
| Post-payment screen: onboarding plan + Calendly booking link | High | 45m |
| Non-buyer screen: soft Substack CTA | High | 30m |
| Confirmation email with onboarding plan (via API email service) | Medium | 1h |

**Funnel after Phase 3:**
```
Assessment complete
  → Full diagnosis shown (free, ungated, excellent quality)
  → "Want more?" CTA
      ├── $49 Stripe → onboarding plan + Calendly CTA
      └── Skip / close → "Let's keep in touch — subscribe to Substack"
```

**New env vars for Phase 3:**
```
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
STRIPE_PRICE_ID=
CALENDLY_URL=https://calendly.com/mafaas/30min
EMAIL_API_KEY=          # Resend or similar — free tier
FROM_EMAIL=
```

---

## Phase 4 — CRM Stub + Distribution (Week 4) ⏳

**Tracer bullet goal:** A Calendly booking auto-appears in the Google Sheet with stage "Calendly Booked."

### M5 — CRM (Google Sheets)

| Task | Priority | Est. |
|------|----------|------|
| Add Pipeline tab to Google Sheet with stage columns | Medium | 30m |
| Calendly webhook → `/api/crm` → update row stage | Medium | 1h |
| Dan updates stages manually via Sheets mobile | Medium | 0 (no code) |

### M6 — Distribution

| Task | Priority | Est. |
|------|----------|------|
| Substack subscribe CTA on assessment completion screen | High | 30m |
| JSON-LD structured data on landing page (SEO) | Medium | 30m |
| `llms.txt` on landing page root (AEO) | Low | 20m |
| Testimonials placeholder section on landing page | Low | 30m |

---

## V3 — Post-May Roadmap 🔮

| Feature | Module | Why deferred |
|---------|--------|--------------|
| WhatsApp / Telegram integration | M1 | Bot API + conversation state management; needs V2 funnel validated first |
| Image generation in diagnosis | M1 | DALL-E 3 adds $0.04/assessment; powerful differentiator but not launch blocker |
| n8n automation workflows | M3/M6 | Email sequences, social auto-posting — overkill until volume justifies |
| Platform migration (edge runtime) | All | Cloudflare Workers or equivalent when current PoC hosts become a bottleneck |
| Meta Ads pixel + lead gen | M6 | Requires ad spend; premature before funnel conversion rates are known |
| AEO deep integration (Manus/Meta) | M6 | Emerging space; monitor but don't build yet |
| Custom CRM tool | M5 | Build when Sheets becomes painful, not before |
| Content generation automation | M6 | Substack → LinkedIn/X auto-share via n8n |

---

## Stack Evolution

```
V1 — PoC (done)
  Static HTML host + Serverless API host + OpenAI

V2 — End of May
  + GA4 (analytics)
  + Google Sheets (leads + CRM)
  + Stripe (payments)
  + /api/events, /api/checkout, /api/webhook, /api/crm
  + Conversational UI
  + Spanish + English

V3 — June+
  + Edge runtime migration (if needed)
  + n8n automation layer
  + WhatsApp / Telegram
  + Meta Pixel + Ads
  + Custom CRM
```
