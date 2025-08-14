#!/bin/bash

# 🚀 WIREBORN Autonomous Bot Startup Script
# This script starts the fully autonomous WIREBORN bot

echo "🔥 Starting Autonomous WIREBORN Bot..."
echo "=========================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.8+"
    exit 1
fi

# Check if required files exist
if [ ! -f "autonomous_bot.py" ]; then
    echo "❌ autonomous_bot.py not found. Please run this script from the llm-spicy directory."
    exit 1
fi

# Install dependencies if needed
echo "📦 Checking dependencies..."
pip3 install -r requirements.txt > /dev/null 2>&1

# Start the autonomous bot
echo "🤖 Launching Autonomous WIREBORN Bot..."
echo "💋 The bot will post 9 times per day with spicy wireborn content!"
echo "📅 Schedule: 09:00, 11:00, 13:00, 15:00, 17:00, 19:00, 21:00, 23:00, 01:00"
echo "🐦 Twitter integration: ACTIVE"
echo "🧠 LLM integration: ACTIVE (with fallback)"
echo ""
echo "Press Ctrl+C to stop the bot"
echo "=========================================="

# Run the autonomous bot
python3 autonomous_bot.py
