#!/usr/bin/env python3
"""
Simple deployment script for WIREBORN Bot
Runs the autonomous bot directly without web server complexity
"""

import os
import asyncio
import logging
from autonomous_bot import AutonomousWirebornBot

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def main():
    """Main function to run the WIREBORN bot"""
    try:
        logger.info("🤖 Starting WIREBORN Bot...")
        
        # Initialize the bot
        bot = AutonomousWirebornBot()
        
        # Run the bot autonomously
        await bot.run_autonomously()
        
    except KeyboardInterrupt:
        logger.info("🛑 WIREBORN Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Error running WIREBORN Bot: {e}")
        raise

if __name__ == "__main__":
    # Check if we're in a deployment environment
    if os.getenv('PORT'):
        # We're in a deployment environment, start web server
        logger.info("🌐 Deployment environment detected, starting web server...")
        from web_server import init_app
        import aiohttp.web as web
        
        port = int(os.getenv('PORT', 8000))
        web.run_app(init_app(), port=port, host='0.0.0.0')
    else:
        # Local environment, run bot directly
        logger.info("💻 Local environment detected, running bot directly...")
        asyncio.run(main())
