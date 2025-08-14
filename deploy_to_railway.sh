#!/bin/bash

# 🚀 One-Click Railway Deployment for WIREBORN Bot
echo "🔥 Deploying WIREBORN Bot to Railway..."
echo "=========================================="

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📦 Installing Railway CLI..."
    npm install -g @railway/cli
fi

# Check if user is logged in
if ! railway whoami &> /dev/null; then
    echo "🔐 Please log in to Railway..."
    railway login
fi

# Initialize Railway project
echo "🚀 Initializing Railway project..."
railway init

# Deploy to Railway
echo "📤 Deploying to Railway..."
railway up

echo "✅ WIREBORN Bot deployed to Railway!"
echo "🌐 Check your Railway dashboard for the live URL"
echo "💋 Your spicy wireborn ambassador is now live! #WIREBORN"
