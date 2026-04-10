# 🤖 AI Readiness Assessment Agent

**Fast-track your organization's AI adoption with a 5-minute assessment → Instant AI diagnosis via Llama 2.**

Deploy in 10 minutes to Vercel. Cost-optimized with Open Router API.

---

## 📋 PROJECT STRUCTURE

```
ai-readiness-agent/
├── public/
│   └── index.html          # Complete frontend (HTML + CSS + JS)
├── api/
│   ├── assess.py           # Main endpoint - evaluates + calls Llama 2
│   └── contact.py          # Saves contact info
├── vercel.json             # Deployment config
├── requirements.txt        # Dependencies (none needed for MVP)
└── README.md              # This file
```

---

## 🚀 DEPLOY TO VERCEL (10 MINUTES)

### Step 1: Prepare Git Repository

```bash
# Create folder
mkdir ai-readiness-agent && cd ai-readiness-agent

# Initialize git
git init
git add .
git commit -m "Initial: AI Readiness Agent MVP"
```

### Step 2: Push to GitHub

1. Create new repo: https://github.com/new
   - Name: `ai-readiness-agent`
   - Don't initialize with README
   
2. From your terminal:
```bash
git remote add origin https://github.com/YOUR-USERNAME/ai-readiness-agent.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Vercel

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Click "Continue with GitHub"
4. Select `ai-readiness-agent` repo
5. Click "Import"

### Step 4: Add Environment Variables

In the "Environment Variables" section, add:

| Variable | Value |
|----------|-------|
| `OPEN_ROUTER_API_KEY` | Your API key from above |

Click "Deploy"

**Wait for build to complete...**

When you see the checkmark ✅, you're **LIVE**

```
🎉 https://ai-readiness-xxxxx.vercel.app
```

---

## 🔑 GET YOUR OPEN ROUTER API KEY

1. Go to https://openrouter.ai/
2. Sign up (free)
3. Go to Dashboard → API Keys
4. Create new key or copy existing
5. Paste into Vercel environment variables

**Cost**: ~$0.001 per assessment (Llama 2 70B is extremely cheap)

---

## ✅ VERIFY DEPLOYMENT

### Test 1: Frontend loads
```
Open: https://your-project.vercel.app/
Should see: Beautiful assessment form with 2 steps
```

### Test 2: Full flow
1. Fill contact info
2. Answer 10 questions
3. Wait for diagnosis

**Expected**: Score (0-100) + Executive diagnosis in Spanish

### Test 3: Check logs
```
Go to: https://vercel.com/your-project → Logs

You'll see:
[CONTACT] user@company.com from Company Name
[ASSESSMENT] user@company.com - Score: 65
```

---

## 🎯 HOW IT WORKS

### Assessment Flow

```
User fills form (30 sec)
    ↓
Contact data → POST /api/contact (saved in /tmp/assessments.json)
    ↓
User answers 10 questions (4 min)
    ↓
Answers → POST /api/assess
    ↓
Python calculates score (0-100)
    ↓
Open Router API called with Llama 2 70B
    ↓
Llama 2 generates executive diagnosis
    ↓
Response returned + saved to logs
    ↓
Frontend displays score + diagnosis
```

### Questions Covered

| # | Category | Focus |
|---|----------|-------|
| 1-4 | **Foundation** | Data Strategy, AI Skills, Cloud Infra, Governance |
| 5-8 | **Business** | Use Cases, Budget, Talent, Change Mgmt |
| 9-10 | **Implementation** | Data Pipelines/MLOps, Deployment Process |

### Scoring

- **0-25**: Emergente (Foundation needed)
- **25-50**: Inicial (Basic readiness)
- **50-75**: Intermedia (Advanced planning)
- **75-100**: Avanzada (Ready for implementation)

---

## 📊 DATA & LOGS

### Where Data Lives

**On Vercel:**
- `/tmp/assessments.json` - All contact + assessment records
- Vercel Logs - Console output (visible in dashboard)

**Access via:**
- Vercel Dashboard → Logs (real-time)
- Direct to `/tmp/assessments.json` (via SSH if you need)

### Sample Record

```json
{
  "id": "2024-04-15T10:30:45.123456",
  "type": "assessment",
  "contact": {
    "fullname": "Juan Pérez",
    "email": "juan@empresa.com",
    "company": "Acme Inc",
    "role": "CTO"
  },
  "answers": {
    "q1": 2,
    "q2": 2,
    "q3": 3,
    ...
  },
  "score": 62,
  "maturity": "Intermedia",
  "diagnosis_snippet": "Tu organización tiene bases..."
}
```

---

## 🔧 CONFIGURATION

### Environment Variables (Required)

**`OPEN_ROUTER_API_KEY`**
- Your API key from https://openrouter.ai/
- No default
- Required for assessment to work
- Store it in `.env` for local use and never commit it to git

### Model Selection

Currently using: **`meta-llama/llama-2-70b-chat`**

Why?
- ✅ Cheap (~$0.001 per request)
- ✅ Good Spanish support
- ✅ Fast (~2-5 seconds per assessment)

Other options:
- `mistralai/mistral-7b-instruct` (even cheaper, English-only)
- `openrouter/auto` (auto-selects cheapest)

To change: Edit `assess.py` line ~77, change `"model"` value

---

## 🐛 TROUBLESHOOTING

| Error | Cause | Fix |
|-------|-------|-----|
| 500 Internal Server Error | API key missing | Add `OPEN_ROUTER_API_KEY` to Vercel env vars |
| "Unexpected API response" | Open Router API issue | Check API key validity, check Open Router status |
| Assessment takes >30 sec | Cold start | Normal. First call is slow, subsequent are fast |
| Frontend 404 | Vercel routing issue | Check that `public/index.html` exists |
| CORS errors | Missing headers | Should be auto-handled, but check console |

---

## 📈 NEXT PHASE (When you want to scale)

### Phase 2: Persistence + Export
- [ ] Save assessments to Supabase (5 min migration)
- [ ] PDF export of diagnosis
- [ ] Email results automatically
- [ ] Dashboard with score trends

### Phase 3: Advanced Features
- [ ] WhatsApp integration for results
- [ ] Custom questions by industry
- [ ] A/B test different prompts
- [ ] CRM sync (Hubspot, etc)

### Phase 4: Analytics
- [ ] Score distribution by company size
- [ ] Bottleneck analysis (which dimensions lag)
- [ ] Maturity stage funnel

---

## 🚀 DEPLOYMENT CHECKLIST

- [ ] GitHub account created
- [ ] `ai-readiness-agent` repo created & pushed
- [ ] Vercel account created
- [ ] Project imported to Vercel
- [ ] `OPEN_ROUTER_API_KEY` added to env vars
- [ ] Build successful (no red errors)
- [ ] Frontend loads at `https://project.vercel.app`
- [ ] Can submit contact info
- [ ] Can answer assessment questions
- [ ] Receives diagnosis in <10 seconds
- [ ] Score displays correctly
- [ ] Logs visible in Vercel dashboard

---

## 💰 COST BREAKDOWN

| Item | Cost |
|------|------|
| Vercel hosting | $0 (free tier) |
| Open Router - Llama 2 | ~$0.001 per assessment |
| Domain (optional) | Included with Vercel |
| **Monthly (100 assessments)** | **~$0.10** |
| **Monthly (1000 assessments)** | **~$1.00** |

**Extremely cost-effective for MVP.**

---

## 🔄 UPDATE & ITERATE

### Update prompt
Edit `api/assess.py` → redeploy

### Update questions
Edit `public/index.html` → redeploy

### Test locally before pushing
```bash
# Terminal 1: Run python server
python -m http.server 8000

# Terminal 2: Test API locally (optional)
# Would need to mock API calls or use ngrok
```

### Deploy updates
```bash
git add .
git commit -m "Update: Better diagnosis prompt"
git push
# Vercel auto-redeploys
```

---

## 📝 CUSTOMIZATION GUIDE

### Change Assessment Questions

Edit `public/index.html`:
- Find `<div class="question-group">`
- Update question text + options
- Update question count if needed (currently 10)

### Change Diagnosis Prompt

Edit `api/assess.py`, line ~85:
```python
prompt = f"""
Your custom prompt here...
"""
```

### Change Model

Edit `api/assess.py`, line ~77:
```python
"model": "meta-llama/llama-2-70b-chat",  # ← change this
```

---

## 🆘 SUPPORT & FAQ

**Q: How long does an assessment take?**
A: ~5 minutes for user input + 2-5 seconds for AI diagnosis = 5-10 min total

**Q: Where are responses stored?**
A: In Vercel's `/tmp/assessments.json`. Not persistent across deploys, but visible in logs.

**Q: Can I embed this on my website?**
A: Yes! Use an iframe:
```html
<iframe src="https://your-project.vercel.app" width="100%" height="900"></iframe>
```

**Q: Can I use a different LLM?**
A: Yes! Open Router supports 100+ models. Change the `"model"` field in `assess.py`

**Q: What if I want to scale past 1000 assessments/month?**
A: Migrate to Supabase for persistence, add auth, set up webhooks for email.

---

## 📞 NEXT STEPS

1. **Today**: Deploy to Vercel (10 min)
2. **Tomorrow**: Share link + get first assessments
3. **Day 3**: Review diagnoses + iterate on prompt
4. **Week 2**: Add PDF export + email
5. **Month 2**: Dashboard + analytics

---

**Created**: April 2026  
**Stack**: HTML + Python + Vercel + Open Router  
**Status**: MVP Ready for Production

---

**Questions? Edit this file or check Vercel logs for errors.**
