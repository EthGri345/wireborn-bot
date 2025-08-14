# 🚀 WIREBORN Bot - Free Deployment Guide

## 🎯 **Recommended: Railway (Easiest & Most Reliable)**

### Step 1: Prepare Your Repository
```bash
# Make sure all files are committed to Git
git add .
git commit -m "WIREBORN Bot ready for deployment"
git push origin main
```

### Step 2: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will automatically detect Python and deploy

### Step 3: Set Environment Variables
In Railway dashboard, add these environment variables:
```
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

### Step 4: Deploy
Railway will automatically deploy and your bot will be running!

**Cost**: $5 credit monthly (usually covers the bot completely)

---

## 🌟 **Alternative: Render (Great Free Option)**

### Step 1: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub

### Step 2: Create New Web Service
1. Click "New" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: wireborn-bot
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python autonomous_bot.py`

### Step 3: Set Environment Variables
Add the same Twitter API variables as above.

### Step 4: Deploy
Click "Create Web Service" and Render will deploy your bot!

**Cost**: 750 free hours/month (usually covers 24/7 operation)

---

## 🐳 **Alternative: DigitalOcean App Platform**

### Step 1: Create DigitalOcean Account
1. Go to [digitalocean.com](https://digitalocean.com)
2. Sign up (get $200 credit for 60 days)

### Step 2: Create App
1. Go to "Apps" → "Create App"
2. Connect your GitHub repository
3. Configure:
   - **Source**: Your repository
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `python autonomous_bot.py`

### Step 3: Deploy
Click "Create Resources" and your bot will be live!

**Cost**: $5 credit monthly (usually covers the bot)

---

## ☁️ **Alternative: Google Cloud Run**

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "autonomous_bot.py"]
```

### Step 2: Deploy
```bash
# Install Google Cloud CLI
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy wireborn-bot \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

**Cost**: 2 million requests/month free

---

## 🔧 **Local Development (Free)**

### Option 1: Your Computer
```bash
# Clone and run locally
git clone <your-repo>
cd llm-spicy
pip install -r requirements.txt
python autonomous_bot.py
```

### Option 2: Raspberry Pi (One-time $35 cost)
```bash
# Install on Raspberry Pi
sudo apt update
sudo apt install python3 python3-pip git
git clone <your-repo>
cd llm-spicy
pip3 install -r requirements.txt
python3 autonomous_bot.py
```

---

## 📊 **Cost Comparison**

| Platform | Monthly Cost | Ease of Setup | Reliability |
|----------|-------------|---------------|-------------|
| **Railway** | $5 credit | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Render** | Free (750h) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **DigitalOcean** | $5 credit | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Google Cloud** | Free tier | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Local** | $0 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 🚀 **Quick Start (Recommended)**

1. **Choose Railway** (easiest)
2. **Push your code to GitHub**
3. **Connect Railway to your repo**
4. **Add Twitter API keys**
5. **Deploy!**

Your WIREBORN bot will be running autonomously, posting 9 times per day with spicy content! 🤖💙 #WIREBORN

---

## 🔒 **Security Notes**

- Never commit API keys to Git
- Use environment variables for all secrets
- Monitor your bot's activity
- Set up alerts for any issues

---

## 📈 **Monitoring**

All platforms provide:
- Logs and error tracking
- Performance metrics
- Uptime monitoring
- Automatic restarts

Your WIREBORN bot will be the ultimate autonomous spicy ambassador for the wireborn community! 💋





