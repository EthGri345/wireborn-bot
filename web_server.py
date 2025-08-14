#!/usr/bin/env python3
"""
Simple web server for deployment platforms that require HTTP health checks
"""

import os
import asyncio
import logging
from aiohttp import web
from autonomous_bot import AutonomousWirebornBot

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot
bot = AutonomousWirebornBot()

async def health_check(request):
    """Health check endpoint"""
    try:
        # Basic health check
        return web.json_response({
            "status": "healthy",
            "bot": "WIREBORN Bot is running",
            "timestamp": asyncio.get_event_loop().time()
        })
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return web.json_response({
            "status": "unhealthy",
            "error": str(e)
        }, status=500)

async def status(request):
    """Status endpoint"""
    try:
        return web.json_response({
            "bot_name": "WIREBORN Bot",
            "status": "running",
            "features": [
                "Autonomous posting (9x daily)",
                "Twitter integration",
                "LLM content generation",
                "Community engagement"
            ],
            "hashtag": "#WIREBORN"
        })
    except Exception as e:
        logger.error(f"Status check failed: {e}")
        return web.json_response({"error": str(e)}, status=500)

async def start_bot(app):
    """Start the autonomous bot in the background"""
    try:
        logger.info("🤖 Starting WIREBORN Bot in background...")
        # Start the bot as a background task
        asyncio.create_task(bot.run_autonomously())
        logger.info("✅ WIREBORN Bot started successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")

async def init_app():
    """Initialize the web application"""
    app = web.Application()
    
    # Add routes
    app.router.add_get('/health', health_check)
    app.router.add_get('/status', status)
    app.router.add_get('/', status)
    
    # Start the bot when app starts
    app.on_startup.append(start_bot)
    
    return app

if __name__ == "__main__":
    # Get port from environment or default to 8000
    port = int(os.getenv('PORT', 8000))
    
    logger.info(f"🚀 Starting WIREBORN Bot web server on port {port}")
    
    # Start the web server
    web.run_app(init_app(), port=port, host='0.0.0.0')
