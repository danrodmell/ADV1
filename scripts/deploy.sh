#!/bin/bash
# deploy-ai-readiness.sh
# Fast deployment helper for AI Readiness Agent

set -e

echo "🤖 AI Readiness Agent - Deployment Helper"
echo "=========================================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git not found. Please install git.${NC}"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo -e "${YELLOW}⚠️  npm not found. You'll need to install Vercel CLI manually.${NC}"
fi

echo -e "${GREEN}✓ Git found${NC}"
echo ""

# Get configuration
read -p "Enter GitHub username: " GITHUB_USER
read -p "Enter your Open Router API Key: " API_KEY

if [ -z "$GITHUB_USER" ] || [ -z "$API_KEY" ]; then
    echo -e "${RED}❌ Missing required information${NC}"
    exit 1
fi

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial: AI Readiness Agent MVP"
else
    echo "✓ Git repository already initialized"
fi

# Add remote
REPO_URL="https://github.com/${GITHUB_USER}/ai-readiness-agent.git"
if ! git remote get-url origin &> /dev/null; then
    echo "📡 Adding remote repository..."
    git remote add origin "$REPO_URL"
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push -u origin main 2>/dev/null || echo "Note: Ensure repo exists on GitHub"

echo ""
echo -e "${GREEN}✓ Repository ready!${NC}"
echo ""
echo "📋 NEXT STEPS:"
echo "1. Go to https://github.com/new"
echo "2. Create repo: ai-readiness-agent"
echo "3. Go to https://vercel.com/dashboard"
echo "4. Click 'Add New' → 'Project'"
echo "5. Select ai-readiness-agent from GitHub"
echo "6. Add environment variable:"
echo "   - OPEN_ROUTER_API_KEY: ${API_KEY:0:10}..."
echo "7. Click Deploy"
echo ""
echo "🎉 Your assessment will be live in 2 minutes!"
echo ""
