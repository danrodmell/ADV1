# Technical Roadmap — Dan Melendez AI Consultancy Distribution Engine
**Version:** 1.0 | **Date:** 2026-05-01 | **Deadline:** End of May 2026

Status legend: ✅ Done · 🔄 In progress · ⏳ Queued · 🔮 V3 (post-May)

---

## Phase 1 — Foundation (Week 1) ✅ COMPLETE

**Tracer bullet goal:** Prove both products are live, connected, and findable.

| Task | Module | Status | Notes |
|------|--------|--------|-------|
| Fix OpenAI model name (gpt-4o-mini) | M1 | ✅ | Was gpt-5-mini — invalid |
| Simplify response parser | M1 | ✅ | Removed OpenRouter-era extract_text() |
| Make MODEL_NAME env-var driven | M1 | ✅ | Defaults to gpt-4o-mini |
| Add meta description + OG tags | M2 | ✅ | Twitter card included |
| Fix nav Substack link | M2 | ✅ | Was plain text span |
| Add assessment CTA to landing page | M2 | ✅ | "digital self-assessment →" |
| Add Netlify _redirects | M2 | ✅ | 404 fallback |
| Create PDR, Governance, Roadmap | Docs | ✅ | This document |

**Manual action required:** Set `OPENAI_API_KEY` in Vercel Project → Settings → Environment Variables.

---

## Phase 2 — Conversational UI + Instrumentation (Week 2) ⏳

**Tracer bullet goal:** One question delivered as a chat message, answer logged to Airtable in real time.

### M1 — Assessment Agent: Conversational upgrade

| Task | Priority | Est. time |
|------|----------|-----------|
| Redesign assessment flow as chat UI (message bubbles, not form) | High | 2h |
| Add typing indicator while waiting for AI response | High | 30min |
| Persist each answer to `/api/events` as user answers (not on submit) | High | 1h |
| Store contact info at step 0 before questions begin | High | 30min |
| Add UTM source capture on session start | Medium | 30min |

**UI spec for conversational flow:**
```
Agent: "Hi, I'm here to assess your company's AI readiness. What's your name?"
User: "Sarah"
Agent: "Great, Sarah. And your email so I can send your results?"
User: "sarah@company.com"
Agent: "Question 1 of 10: Does your company have a documented data strategy?"
  [A] No documented strategy
  [B] Informal understanding
  [C] Formal, documented strategy
```

### M3 — Analytics & Instrumentation

| Task | Priority | Est. time |
|------|----------|-----------|
| Add Plausible script to landing page | High | 30min |
| Add Plausible script to assessment (public/index.html) | High | 30min |
| Track custom events: `assessment_start`, `email_captured`, `assessment_complete` | High | 1h |
| Create `/api/events` endpoint (Vercel) → write to Airtable | High | 1h |
| Set up Airtable base: Leads table with schema from PDR | High | 30min |

**New env vars for Phase 2:**
```
AIRTABLE_API_KEY=
AIRTABLE_BASE_ID=
PLAUSIBLE_DOMAIN=
```

---

## Phase 3 — Monetization (Week 3) ⏳

**Tracer bullet goal:** One test payment of $49 via Stripe unlocks the implementation roadmap section.

### M4 — Paywall + Stripe

| Task | Priority | Est. time |
|------|----------|-----------|
| Set up Stripe product ($49, "AI Readiness Implementation Roadmap") | High | 30min |
| Add `/api/checkout` endpoint → creates Stripe Checkout session | High | 1h |
| Add `/api/webhook` endpoint → handles Stripe payment success | High | 1h |
| Gate "Implementation Roadmap" section in assessment results behind payment | High | 1h |
| Post-payment: show full roadmap + Calendly CTA in browser | High | 30min |
| Route free-tier completions to Substack subscribe CTA | High | 30min |
| Send confirmation email with roadmap PDF on payment success | Medium | 1h |

**Funnel flow after Phase 3:**
```
Assessment complete
  ├── FREE: Score + summary diagnosis + "Subscribe to Substack" CTA
  └── PAID ($49 Stripe): Full diagnosis + implementation roadmap + Calendly CTA
```

**New env vars for Phase 3:**
```
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
STRIPE_PRICE_ID=
CALENDLY_URL=https://calendly.com/mafaas/30min
```

---

## Phase 4 — CRM Stub + Distribution (Week 4) ⏳

**Tracer bullet goal:** A Calendly booking auto-appears as a new row in Airtable with stage "Calendly Booked."

### M5 — CRM (Airtable)

| Task | Priority | Est. time |
|------|----------|-----------|
| Airtable pipeline view: Assessment → $49 → Calendly Booked → Proposal → Closed | Medium | 30min |
| Calendly webhook → `/api/crm` → update Airtable lead stage | Medium | 1h |
| Manual stage update instructions for Dan (Airtable mobile) | Medium | 30min |

### M6 — Distribution

| Task | Priority | Est. time |
|------|----------|-----------|
| Add Substack subscribe embed/link to assessment completion screen | High | 30min |
| Add structured data (JSON-LD) to landing page for SEO | Medium | 30min |
| Add `llms.txt` to landing page for AEO | Low | 30min |
| Testimonials section placeholder on landing page | Low | 30min |

---

## V3 — Post-May Roadmap 🔮

These are validated future bets. They should not block May launch.

| Feature | Module | Why deferred |
|---------|--------|--------------|
| WhatsApp / Telegram integration | M1 | Requires Bot API setup + conversation state management |
| Image generation in diagnosis | M1 | DALL-E 3 adds $0.04/assessment; valuable but not launch blocker |
| n8n automation workflows | M3/M6 | Valuable for email sequences and social posting; overkill for V2 |
| Cloudflare Workers migration | M1 | Better cold start, lower cost at scale; not needed at current volume |
| Meta Ads pixel + lead gen | M6 | Requires ad spend; premature before funnel is validated |
| AEO deep integration (Manus/Meta) | M6 | Emerging space; monitor but don't build yet |
| Content generation automation | M6 | Substack → LinkedIn auto-share; n8n or Zapier |
| Full CRM with email sequences | M5 | Airtable + n8n when deal volume justifies |

---

## Stack Evolution

```
V1 (Now)
  Vercel Python + Netlify static + OpenAI

V2 (End of May)
  + Airtable (leads + CRM)
  + Stripe (payments)
  + Plausible (analytics)
  + /api/events, /api/checkout, /api/webhook, /api/crm (new Vercel endpoints)

V3 (June+)
  + n8n (automation layer)
  + Cloudflare Workers (consider migration from Vercel)
  + WhatsApp Business API or Telegram Bot
  + Meta Pixel
```

---

## Open Questions (for Dan to decide before Phase 2)

1. **Analytics tool:** Plausible ($9/month) or GA4 (free, requires cookie consent banner)?
2. **Lead store:** Airtable (free tier, 1,000 records) or Notion DB (already have access)?
3. **Assessment language:** Keep Spanish or add English version for wider reach?
4. **Substack CTA copy:** What's the Substack value prop for non-buyers? ("Read my analysis of 180 companies..." or something else?)
5. **Vercel URL for assessment:** What is the live ADV1 URL? Needed to finalize the landing page CTA link.
