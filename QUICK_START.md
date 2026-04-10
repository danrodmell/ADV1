# ⚡ QUICK START: Live in 10 Minutes

## YOU HAVE:
- ✅ Open Router API Key: `YOUR_OPEN_ROUTER_API_KEY`
- ✅ LangChain docs (for reference)
- ✅ This project (complete & ready)

## STEP 1: Create GitHub Repo (1 min)

1. Go to https://github.com/new
2. Name: `ai-readiness-agent`
3. Description: "AI organization readiness assessment tool"
4. Click "Create repository"

**COPY the SSH or HTTPS URL from the next page**

## STEP 2: Push Code to GitHub (2 min)

```bash
cd ai-readiness-agent/
git init
git add .
git commit -m "Initial: AI Readiness Agent MVP"
git remote add origin https://github.com/YOUR-USERNAME/ai-readiness-agent.git
git branch -M main
git push -u origin main
```

## STEP 3: Deploy to Vercel (5 min)

### Option A: Via Vercel Dashboard (Easiest)

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Click "Continue with GitHub"
4. Find and select `ai-readiness-agent`
5. Click "Import"
6. Under "Environment Variables" add:
   - **Name**: `OPEN_ROUTER_API_KEY`
   - **Value**: `YOUR_OPEN_ROUTER_API_KEY`
7. Click "Deploy"

**WAIT ~1-2 minutes for build...**

When you see the checkmark ✅:
```
🎉 https://ai-readiness-xxxxx.vercel.app
```

### Option B: Via Vercel CLI (1 min)

```bash
npm i -g vercel
vercel login
cd ai-readiness-agent
vercel

# Follow prompts, add env var when asked
# Done!
```

## STEP 4: Verify It Works (2 min)

1. Open: `https://your-project.vercel.app`
2. Fill contact info (test@example.com)
3. Answer 5 questions
4. Click Submit
5. **Should see**: Score + Diagnosis in <10 seconds

## ✅ DONE!

Your AI Assessment Agent is **LIVE**.

---

## WHAT YOU NOW HAVE

| Component | Location | Purpose |
|-----------|----------|---------|
| Frontend | `public/index.html` | Beautiful assessment form |
| API 1 | `api/contact.py` | Saves user contact |
| API 2 | `api/assess.py` | Calls Llama 2 + generates diagnosis |
| Config | `vercel.json` | Deployment configuration |

## NEXT: USE IT

### Share the link
```
https://your-project.vercel.app
```

### View responses
1. Go to Vercel Dashboard → Your Project
2. Click "Logs" tab
3. See every assessment in real-time

### Check data
Assessments stored in `/tmp/assessments.json` on Vercel (visible in logs)

---

## QUICK REFERENCE

| Action | How To |
|--------|--------|
| Change questions | Edit `public/index.html` |
| Improve diagnosis | Edit `api/assess.py` (line 85) |
| Switch LLM model | Edit `api/assess.py` (line 77) |
| Add new endpoint | Create `api/newname.py` in Vercel |
| See logs | Vercel Dashboard → Logs |
| Custom domain | Vercel Dashboard → Settings → Domains |

---

## TROUBLESHOOTING

**Q: Build failed in Vercel?**
A: Check that `OPEN_ROUTER_API_KEY` is set. Redeploy.

**Q: Assessment page shows 404?**
A: Refresh browser. Vercel might still be deploying.

**Q: API times out?**
A: Normal on first request (cold start). Takes 2-5 sec after.

**Q: Can't see responses?**
A: Check Vercel Logs (dashboard → Logs tab)

---

## COST

| Item | Cost |
|------|------|
| Vercel hosting | FREE |
| Llama 2 per assessment | ~$0.0005 |
| First 100 assessments | ~$0.05 |
| Monthly (1000 assessments) | ~$0.50 |

**Essentially free for MVP.**

---

## YOU'RE DONE! 🎉

Your AI Readiness Assessment Agent is live and getting responses.

**Next phase**: Add email follow-up, PDF export, dashboard analytics.

But for now: **SHIP IT!**

Share the link and start collecting assessments.

---

**GitHub**: https://github.com/danrodmell/ai-readiness-agent  
**Live**: https://your-project.vercel.app  
**API Key**: Set in Vercel ✅  
**Status**: READY FOR PRODUCTION  
