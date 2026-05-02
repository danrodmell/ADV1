# Product Design & Requirements — Dan Melendez AI Consultancy Distribution Engine
**Version:** 1.0 | **Date:** 2026-05-01 | **Status:** Approved for development

---

## 1. Problem & Opportunity

Dan Melendez has deep expertise in AI implementation, venture capital, and startup operations from zero to growth stage. The gap is not capability — it is distribution. Converting that expertise into a repeatable revenue engine requires a systematic funnel that qualifies leads, captures intent at every touchpoint, and converts the right buyers at the right price point.

**Current state:**
- Two working MVPs: AI Readiness Assessment (Vercel) + Marketing Landing Page (Netlify)
- No funnel instrumentation — no visibility into drop-off, conversion, or intent signals
- No monetization layer — free assessment with no upgrade path
- No automation — every lead requires manual follow-up

**Opportunity:** Build a distribution engine where the assessment is the hook, the diagnosis is the paywall trigger, and the Calendly call closes the consultancy sprint.

---

## 2. Business Model

| Tier | Product | Price | Conversion Goal |
|------|---------|-------|-----------------|
| Free | AI Readiness Score + summary diagnosis | $0 | Substack subscriber |
| Paid | Full diagnosis + implementation roadmap | $49 | Calendly call booked |
| Enterprise | Quarterly consultancy sprint | $6,000–$9,000 | Closed deal |

**Target customer:**
- Seed and above founders looking to improve unit economics through better shipping or leaner operations
- Traditional companies with $1M+ ARR facing the same need

**Non-customer path:** Everyone who completes the free assessment and doesn't convert to $49 should be routed to the Substack. They are future pipeline.

---

## 3. Product Modules

The system is composed of six independent, embeddable modules. Each module has one purpose and communicates with others only through defined interfaces (API calls, webhook events, or shared data schema).

---

### M1 — Assessment Agent (Lead Qualification Hook)

**Purpose:** Qualify leads and generate enough intent signal to convert to the $49 tier.

**Current state:** Working Vercel deployment with 10-question form → OpenAI diagnosis.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M1-F1 | Conversational UI: chat-like message-by-message flow (not a form) | High |
| M1-F2 | Collect contact info (name, email, company, role) at step 1 | High |
| M1-F3 | Persist every answer to a datastore in real time (not on submit) | High |
| M1-F4 | Return a scored diagnosis (0–100, maturity tier) | High |
| M1-F5 | Show full diagnosis for free (Tier 0) | High |
| M1-F6 | Gate implementation roadmap behind $49 paywall (Tier 1) | Medium |
| M1-F7 | Trigger Calendly CTA upon Tier 1 payment | Medium |
| M1-F8 | Route free-tier completions to Substack subscribe CTA | Medium |
| M1-F9 | Visual diagnosis output (charts, maturity grid, generated image) | Low |
| M1-F10 | Embeddable as iframe or web component in the landing page | Medium |
| M1-F11 | Works in WhatsApp and Telegram without UI changes | Low |

**Non-functional requirements:**
- Response time for diagnosis: < 8 seconds
- Mobile-first — 70%+ of leads will arrive via social/mobile
- Zero external frontend dependencies (vanilla JS, keep deploy simple)
- All user data stored before the LLM call — if the API fails, the lead is not lost

**Data collected per session:**
```
session_id, timestamp, name, email, company, role,
q1..q10 (each with value + timestamp),
score, maturity, diagnosis, tier_converted, source_utm
```

**Success metrics:**
- Assessment completion rate > 60%
- Email capture rate > 80% of completions
- Tier 1 ($49) conversion rate > 5% of completions
- Calendly booking rate > 40% of Tier 1 purchases

---

### M2 — Landing Page (Distribution Hub)

**Purpose:** Capture intent from cold traffic and route visitors into the funnel.

**Current state:** Single-file HTML on Netlify with Calendly CTA and Substack link. OG/meta tags added.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M2-F1 | Analytics event tracking on every CTA click (Calendly, Substack, Assessment) | High |
| M2-F2 | Scroll depth and time-on-page instrumentation | High |
| M2-F3 | Embedded or linked assessment agent (M1) | High |
| M2-F4 | Testimonials section (placeholder, populated when available) | Medium |
| M2-F5 | Social proof: client logos or case study excerpts | Medium |
| M2-F6 | UTM parameter pass-through to assessment | Medium |
| M2-F7 | Cookie-less analytics (Plausible or equivalent) | High |

**Non-functional requirements:**
- Page load < 2s on mobile (Lighthouse score > 85)
- No JavaScript frameworks — single file or CSS + JS split only
- Stays on Netlify (free tier, no build step required)

**Success metrics:**
- Assessment start rate from landing page > 20% of sessions
- Substack CTA click rate > 8% of sessions
- Calendly click rate > 3% of sessions

---

### M3 — Analytics & Feedback Loops (Instrumentation)

**Purpose:** Give every touchpoint a feedback signal. No dark funnels.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M3-F1 | Plausible Analytics (or GA4) on landing page and assessment | High |
| M3-F2 | Server-side event log for every assessment step (already partial in Vercel logs) | High |
| M3-F3 | Airtable or Notion DB as structured lead store | High |
| M3-F4 | Webhook from assessment → lead store on email capture | High |
| M3-F5 | Weekly automated summary report (n8n or cron) | Low |

**Data flow:**
```
Assessment step completion
  → POST /api/events (Vercel)
    → Airtable (lead record)
    → Plausible (event)
Landing page click
  → Plausible custom event
```

---

### M4 — Monetization Layer (Paywall + Payments)

**Purpose:** Convert qualified leads to revenue at the $49 price point.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M4-F1 | Stripe Checkout for $49 tier | High |
| M4-F2 | Webhook: Stripe payment success → unlock full diagnosis | High |
| M4-F3 | Email delivery of implementation roadmap on payment | High |
| M4-F4 | Calendly link in post-payment confirmation email | High |
| M4-F5 | Failed payment graceful fallback to free tier | Medium |

**Payment flow:**
```
User completes assessment (free diagnosis shown)
  → CTA: "Get your implementation roadmap — $49"
    → Stripe Checkout (hosted page)
      → Payment success webhook → Vercel /api/unlock
        → Full diagnosis + roadmap emailed
        → Calendly CTA shown in browser
```

---

### M5 — CRM (Post-Conversion Tracking)

**Purpose:** Track leads from Calendly booking through consultancy close. Internal only.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M5-F1 | Airtable base with lead pipeline stages | Medium |
| M5-F2 | Auto-populate from M4 Stripe webhook | Medium |
| M5-F3 | Calendly event → update lead stage | Medium |
| M5-F4 | Manual stage update by Dan (mobile-friendly) | Medium |

**Pipeline stages:** `Assessment → $49 → Calendly Booked → Call Completed → Proposal Sent → Closed Won / Lost → Substack`

---

### M6 — Content & Distribution Automation

**Purpose:** Drive cold traffic into the funnel without manual effort.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M6-F1 | Substack post → auto-share to LinkedIn and X | Low |
| M6-F2 | Assessment completion → Substack subscribe prompt | High |
| M6-F3 | SEO optimization: structured data, sitemap, canonical tags | Medium |
| M6-F4 | Meta Ads integration (pixel + lead gen form) | Low |
| M6-F5 | AEO (Agentic Engine Optimization): llms.txt, agent-readable schema | Low |

---

## 4. Technical Architecture

### Current (V1)
```
Netlify (static)          Vercel (serverless Python)
  dan_melendez_ai_readiness.html    /api/assess.py (OpenAI gpt-4o-mini)
  _redirects                        /api/contact.py
```

### Target (V2, End of May)
```
Netlify                   Vercel                    External Services
  Landing page     →       /api/assess              OpenAI (diagnosis)
  (Plausible)      →       /api/events              Stripe (payments)
                   →       /api/unlock              Airtable (leads/CRM)
                            ↓                        Plausible (analytics)
                          Airtable                  Calendly (booking)
```

### Target (V3, June+)
```
Cloudflare Workers        n8n (automation)          Channels
  Edge functions    ←→     Workflows         →       WhatsApp
  (lower latency)          - Lead scoring            Telegram
                           - Email sequences          Meta Ads
                           - Substack sync            LinkedIn
```

### Stack decisions

| Decision | Choice | Rationale | Alternative considered |
|----------|--------|-----------|----------------------|
| Backend | Vercel Python serverless | Already working, zero infra ops | Cloudflare Workers (better for V3) |
| Frontend | Netlify static | Free, zero build step | Vercel static (would consolidate) |
| LLM | OpenAI gpt-4o-mini | Cheap ($0.15/1M tokens), reliable | Anthropic Claude (better quality, higher cost) |
| Analytics | Plausible | Cookie-less, GDPR-clean, $9/month | GA4 (free but complex, cookie consent required) |
| Payments | Stripe | Standard, Webhooks simple | Paddle (better for EU VAT, overkill now) |
| Lead store | Airtable | Mobile-friendly, Dan can edit directly | Notion (slower API), Supabase (overkill V2) |
| Automation | n8n | Self-hostable, powerful, one-time cost | Zapier (expensive at scale), Make (mid) |

---

## 5. Constraints

| Constraint | Value | Impact |
|-----------|-------|--------|
| Development capacity | 2–4 hours/week | ~16 hours total through end of May |
| Deadline | End of May 2026 | 4 sprints of ~4 hours each |
| Budget | Minimize licenses | Free tiers preferred; pay only for Plausible + OpenAI API |
| Stack philosophy | Modular, embeddable | Each module deployable independently |
| Dan's involvement | Stakeholder, not developer | Briefing per module; agent implements |

---

## 6. Out of Scope (V1)

- Mobile app (WhatsApp/Telegram integration is V3)
- Image generation in diagnosis (V3)
- Full CRM with email sequences (V3)
- Testimonials (requires clients — placeholder only)
- Meta Ads pixel (V3)
- Multi-language support (assessment is in Spanish; landing page in English — intentional for now)
