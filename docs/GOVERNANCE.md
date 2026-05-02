# Project Governance — Dan Melendez AI Consultancy Distribution Engine
**Version:** 1.0 | **Date:** 2026-05-01

---

## 1. Roles

| Role | Who | Responsibilities |
|------|-----|-----------------|
| Product Owner / Stakeholder | Dan Melendez | Module scope briefs, pricing decisions, client relationships, final approval on all shipped code |
| Implementing Agent | Claude (AI) | Technical implementation, documentation, code review, tracer bullets |

**Principle:** Dan owns the "what" and "why." The agent owns the "how." Ambiguity in scope stays with Dan — the agent asks, not assumes.

---

## 2. Working Cadence

**Session model:** Each working session is a focused 2–4 hour block.

### Session structure (Tracer Bullet protocol)
1. **Brief** — Dan provides the module scope (1–3 paragraphs, like today)
2. **Explore** — Agent reads current state, surfaces gaps and questions
3. **Minimal slice** — Agent implements the thinnest vertical slice that proves the module end-to-end
4. **Validate** — Dan reviews in preview/browser before expansion
5. **Expand** — Agent fills out the full feature based on validated slice
6. **Ship** — PR opened, Dan merges

**No feature is implemented without a brief. No PR is pushed without Dan reviewing the tracer bullet.**

---

## 3. Decision Framework

### When the agent decides autonomously
- File structure and naming within established patterns
- Code refactoring that doesn't change behavior
- Documentation updates
- Dependency choices within approved stack (see PDR §4)

### When the agent proposes and Dan approves
- New modules or significant feature additions
- Stack changes (new external service, new dependency)
- Pricing or funnel logic changes
- Any change visible to end users

### When Dan decides alone
- Pricing tiers and thresholds
- Client relationships and Calendly handling
- Substack content and posting schedule
- Which consultancy deals to pursue

---

## 4. Branching & Deployment

```
main ──────────────────────────────────→  production
  └── claude/<session-name>  (PR per session)
        └── docs/, api/, public/
```

- **Vercel:** Auto-deploys on merge to `main`
- **Netlify:** Connected to `main` or manual drag-and-drop for HTML-only changes
- **PR rule:** One PR per session. PRs contain the full scope of that session's work including docs updates.

---

## 5. Documentation Standards

Every module ships with:
1. Requirements in PDR (updated before implementation)
2. A `HANDOFF_<module>_<date>.md` if the session ends mid-implementation
3. Updated ROADMAP.md (tick completed items, add new discoveries)

**Document ownership:** Agent writes and maintains all technical docs. Dan reviews and approves changes to PDR business sections (pricing, targets, out-of-scope decisions).

---

## 6. Quality Gates

Before any feature is merged:
- [ ] Tracer bullet validated by Dan in browser or preview
- [ ] No breaking changes to existing endpoints (check `api/assess.py`, `api/contact.py`)
- [ ] New env vars documented in PDR and in a `.env.example` file
- [ ] PR description covers what changed, why, and any manual steps required

---

## 7. Capacity Budget

| Phase | Weeks | Hours | Deliverable |
|-------|-------|-------|-------------|
| Phase 1 | Week 1 (now) | 2–4h | Agent fix + landing SEO ✅ |
| Phase 2 | Week 2 | 2–4h | Analytics + conversational UI |
| Phase 3 | Week 3 | 2–4h | $49 paywall + Stripe |
| Phase 4 | Week 4 | 2–4h | CRM stub + Substack integration |
| Buffer | Post-May | — | V3 features (WhatsApp, image gen, Meta) |

**Rule:** If a phase runs over time budget, scope is cut to maintain the deadline. Dan decides what gets cut.

---

## 8. External Services Approval

Any new paid service requires Dan's explicit approval before integration. Current approved list:

| Service | Purpose | Cost | Status |
|---------|---------|------|--------|
| OpenAI | LLM for diagnosis | ~$0.01/assessment | Active |
| Vercel | API hosting | Free tier | Active |
| Netlify | Landing page hosting | Free tier | Active |
| Plausible | Analytics | $9/month or self-host | Pending approval |
| Stripe | Payments | 2.9% + $0.30/transaction | Pending |
| Airtable | Lead store / CRM | Free tier | Pending |
| n8n | Automation (V3) | Self-host or $20/month | Future |
