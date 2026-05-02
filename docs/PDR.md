# Product Design & Requirements — Dan Melendez AI Consultancy Distribution Engine
**Version:** 1.1 | **Date:** 2026-05-01 | **Status:** Approved for development

---

## 1. Problem & Opportunity

Dan Melendez has deep expertise in AI implementation, venture capital, and startup operations from zero to growth stage. The gap is not capability — it is distribution. Converting that expertise into a repeatable revenue engine requires a systematic funnel that qualifies leads, captures intent at every touchpoint, and converts the right buyers at the right price point.

**Current state (PoC — not locked in):**
- AI Readiness Assessment running as a serverless Python API with a static HTML frontend
- Marketing landing page hosted as a single HTML file
- No funnel instrumentation — no visibility into drop-off, conversion, or intent signals
- No monetization layer — free assessment with no upgrade path
- No automation — every lead requires manual follow-up

> **Stack note:** The current deployment on Vercel (API) and Netlify (landing page) is a proof of concept only. Neither platform is a committed architecture decision. Every module is designed to be portable — see §4 for evolution path.

**Opportunity:** Build a distribution engine where the assessment is the hook, the quality of the diagnosis earns trust, and the onboarding plan + call is the first revenue event.

---

## 2. Business Model

| Tier | Product | Price | Conversion Goal |
|------|---------|-------|-----------------|
| Free | Full AI Readiness diagnosis (score + maturity + LLM analysis) | $0 | Substack subscriber |
| Paid | Onboarding plan + implementation call booking (Calendly) | $49 | Calendly call completed |
| Enterprise | Quarterly consultancy sprint | $6,000–$9,000 | Closed deal |

**Funnel logic:** The diagnosis is ungated and excellent — it earns trust. After the results, the CTA is "Want more?" The $49 buys the personalized onboarding plan and the implementation call. Non-buyers get a soft Substack prompt: *"Let's keep in touch — I'm sure you'll find something valuable."*

**Target customer:**
- Seed and above founders looking to improve unit economics through better shipping or leaner operations
- Traditional companies with $1M+ ARR facing the same need

**Non-customer path:** Everyone who completes the free assessment and doesn't convert to $49 is routed to the Substack. They are future pipeline, not lost leads.

---

## 3. Product Modules

The system is composed of six independent, embeddable modules. Each module has one purpose and communicates with others only through defined interfaces (API calls, webhook events, or shared data schema).

---

### M1 — Assessment Agent (Lead Qualification Hook)

**Purpose:** Qualify leads through a conversational assessment and deliver a diagnosis compelling enough to trigger the $49 upgrade.

**Current state:** Working PoC with 10-question form → OpenAI gpt-4o-mini diagnosis. Live at `https://adv-1-lac.vercel.app/`.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M1-F1 | Conversational UI: chat-like message-by-message flow, not a form | High |
| M1-F2 | Collect contact info (name, email, company, role) conversationally at start | High |
| M1-F3 | Persist every answer to datastore in real time — not on submit | High |
| M1-F4 | Return full scored diagnosis (0–100, maturity tier, LLM analysis) — fully ungated | High |
| M1-F5 | Post-diagnosis CTA: "Want more?" → $49 onboarding plan + Calendly call | High |
| M1-F6 | Stripe Checkout triggered by $49 CTA | Medium |
| M1-F7 | Post-payment: deliver onboarding plan + show Calendly booking link | Medium |
| M1-F8 | Non-buyer CTA: soft Substack subscribe prompt | Medium |
| M1-F9 | Both languages: Spanish and English (auto-detect or toggle) | Medium |
| M1-F10 | Embeddable as iframe or web component in the landing page | Medium |
| M1-F11 | Visual diagnosis output (charts, maturity grid, generated image) | Low |
| M1-F12 | Works in WhatsApp and Telegram without UI changes | Low |

**Non-functional requirements:**
- Response time for diagnosis: < 8 seconds
- Mobile-first — 70%+ of leads will arrive via social/mobile
- Zero external frontend dependencies (vanilla JS, keep deploy simple)
- All user data stored before the LLM call — if the API fails, the lead is not lost

**Data collected per session:**
```
session_id, timestamp, name, email, company, role, language,
q1..q10 (each with value + timestamp),
score, maturity, diagnosis, tier_converted, source_utm
```

**Success metrics:**
- Assessment completion rate > 60%
- Email capture rate > 80% of completions
- $49 conversion rate > 5% of completions
- Calendly booking rate > 40% of $49 purchases

---

### M2 — Landing Page (Distribution Hub)

**Purpose:** Capture intent from cold traffic and route visitors into the funnel.

**Current state:** Single-file HTML with Calendly CTA, Substack link, OG/meta tags. Live at `https://beamish-starlight-f50127.netlify.app/`.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M2-F1 | GA4 event tracking on every CTA click (Calendly, Substack, Assessment) | High |
| M2-F2 | Scroll depth and time-on-page via GA4 | High |
| M2-F3 | Embedded or linked assessment agent (M1) | High |
| M2-F4 | UTM parameter pass-through to assessment session | Medium |
| M2-F5 | Testimonials section (placeholder, populated when available) | Medium |
| M2-F6 | Social proof: client logos or case study excerpts | Medium |
| M2-F7 | Cookie consent banner (required for GA4) | High |

**Non-functional requirements:**
- Page load < 2s on mobile (Lighthouse score > 85)
- No JavaScript frameworks — single file or CSS + JS split only
- Platform-agnostic static HTML — deployable anywhere

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
| M3-F1 | GA4 on landing page and assessment | High |
| M3-F2 | Server-side event log for every assessment step | High |
| M3-F3 | Google Sheets as structured lead store (start simple, migrate later) | High |
| M3-F4 | Assessment → Google Sheets row on email capture | High |
| M3-F5 | Weekly automated summary report | Low |

**Data flow:**
```
Assessment step completion
  → POST /api/events
    → Google Sheets (lead record via Sheets API)
    → GA4 (custom event via Measurement Protocol)
Landing page click
  → GA4 gtag event
```

---

### M4 — Monetization Layer ($49 Paywall)

**Purpose:** Convert qualified leads to the first revenue event at $49.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M4-F1 | Stripe Checkout for $49 ("AI Readiness Onboarding Plan + Call") | High |
| M4-F2 | Payment success webhook → generate and deliver onboarding plan | High |
| M4-F3 | Post-payment: Calendly booking link shown in browser | High |
| M4-F4 | Confirmation email with onboarding plan on payment success | High |
| M4-F5 | Failed payment graceful fallback — no broken state | Medium |

**Funnel flow:**
```
User completes assessment
  → Full diagnosis displayed (free, ungated)
  → CTA: "Want more? Get your onboarding plan + implementation call — $49"
    → Stripe Checkout
      → Payment success → /api/webhook
        → Onboarding plan delivered (in-browser + email)
        → Calendly CTA: "Book your implementation call"
  → Non-buyer: soft Substack CTA
```

---

### M5 — CRM (Post-Conversion Tracking)

**Purpose:** Track leads from Calendly booking through consultancy close. Internal only.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M5-F1 | Google Sheets pipeline tab with lead stages | Medium |
| M5-F2 | Auto-populate from M4 Stripe webhook | Medium |
| M5-F3 | Calendly webhook → update lead stage in Sheets | Medium |
| M5-F4 | Dan updates stages manually on mobile (Sheets mobile app) | Medium |

**Pipeline stages:** `Assessment → $49 Paid → Calendly Booked → Call Completed → Proposal Sent → Closed Won / Lost → Substack`

> **Note:** Google Sheets is the starting point. When deal volume justifies it, this migrates to a proper CRM tool (or a custom-built one).

---

### M6 — Content & Distribution Automation

**Purpose:** Drive cold traffic into the funnel without manual effort per post.

**Functional requirements:**

| ID | Requirement | Priority |
|----|-------------|----------|
| M6-F1 | Assessment completion → Substack subscribe CTA | High |
| M6-F2 | SEO: structured data (JSON-LD), sitemap, canonical tags on landing page | Medium |
| M6-F3 | AEO: `llms.txt` on landing page for AI crawler discoverability | Low |
| M6-F4 | Substack post → auto-share to LinkedIn and X | Low |
| M6-F5 | Meta Ads pixel + lead gen form integration | Low |

---

## 4. Technical Architecture

### PoC (Current — not permanent)
```
Static HTML host          Serverless API host
  Landing page              /api/assess  (OpenAI gpt-4o-mini)
  _redirects                /api/contact
```

### V2 Target (End of May)
```
Static HTML host          API layer                  External Services
  Landing page (GA4) →     /api/assess              OpenAI (diagnosis)
                    →       /api/events              Stripe (payments)
                    →       /api/checkout            Google Sheets (leads/CRM)
                    →       /api/webhook             GA4 (analytics)
                    →       /api/crm                 Calendly (booking)
                             ↓
                           Google Sheets
```

### V3 Target (June+)
```
Edge runtime              Automation layer          Channels
  API functions     ←→     n8n workflows    →       WhatsApp
  (low latency)            - Lead scoring            Telegram
                           - Email sequences          Meta Ads
                           - Substack sync            LinkedIn
```

### Stack philosophy

**Not married to any current host.** Vercel and Netlify are PoC scaffolding. Every module is designed to be portable:
- API layer can move to Cloudflare Workers, Railway, Fly.io, or any serverless provider
- Frontend can be hosted on any static CDN
- The only coupling is through environment variables and HTTP interfaces

| Decision | V2 Choice | Rationale | V3 path |
|----------|-----------|-----------|---------|
| API runtime | Current PoC host | Zero migration cost for V2 | Cloudflare Workers (edge, cheaper at scale) |
| Frontend host | Current PoC host | Static file, deploy anywhere | Any CDN |
| LLM | OpenAI gpt-4o-mini | $0.15/1M tokens, reliable | Anthropic Claude (richer output when justified) |
| Analytics | GA4 | Free, widely understood | Stay GA4 unless privacy requirements change |
| Lead store | Google Sheets | Zero setup, Dan can read on mobile | Custom tool or proper DB when volume hits |
| Payments | Stripe | Standard, webhooks simple | Stay Stripe |
| Automation | Manual / cron | Premature to add n8n before volume | n8n self-hosted (V3) |

---

## 5. Constraints

| Constraint | Value | Impact |
|-----------|-------|--------|
| Development capacity | 2–4 hours/week | ~16 hours total through end of May |
| Deadline | End of May 2026 | 4 sprints of ~4 hours each |
| Budget | Minimize licenses | OpenAI API + Stripe fees only for V2; everything else free tier |
| Stack philosophy | Modular, embeddable, portable | No platform lock-in |
| Dan's involvement | Stakeholder, not developer | Briefing per module; agent implements |

---

## 6. Out of Scope (V2)

- Mobile app (WhatsApp/Telegram integration is V3)
- Image generation in diagnosis (V3)
- Full CRM with email sequences (V3)
- Testimonials (requires clients — placeholder only in V2)
- Meta Ads pixel (V3)
- n8n automation (V3)
