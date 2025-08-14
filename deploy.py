#!/usr/bin/env python3
"""
WIREBORN Bot Deployment Script
Runs the spicy wireborn bot with Twitter integration and scheduling
"""

import asyncio
import logging
import schedule
import time
from datetime import datetime
from wireborn_bot import WirebornBot
from twitter_integration import TwitterIntegration

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class WirebornBotDeployment:
    def __init__(self):
        self.bot = WirebornBot()
        self.twitter = TwitterIntegration()
        self.running = False

    async def start_bot(self):
        """Start the wireborn bot"""
        logger.info("🔥 Starting WIREBORN Bot - Your Spicy AI Ambassador")
        self.running = True
        
        # Schedule daily activities
        schedule.every().day.at("09:00").do(self.daily_spice_report)
        schedule.every().day.at("15:00").do(self.community_engagement)
        schedule.every().day.at("21:00").do(self.evening_spice)
        
        # Schedule hourly token updates
        schedule.every().hour.do(self.token_update)
        
        logger.info("📅 Scheduled activities:")
        logger.info("   - 09:00: Daily Spice Report")
        logger.info("   - 15:00: Community Engagement")
        logger.info("   - 21:00: Evening Spice")
        logger.info("   - Every hour: Token Updates")
        
        # Run scheduled tasks
        while self.running:
            schedule.run_pending()
            await asyncio.sleep(60)  # Check every minute

    async def daily_spice_report(self):
        """Post daily spice report"""
        try:
            logger.info("📊 Posting daily spice report...")
            await self.twitter.schedule_daily_spice_report()
            logger.info("✅ Daily spice report posted successfully")
        except Exception as e:
            logger.error(f"❌ Failed to post daily spice report: {e}")

    async def community_engagement(self):
        """Engage with wireborn community"""
        try:
            logger.info("💬 Engaging with wireborn community...")
            reply_count = await self.bot.engage_with_wireborn_community()
            logger.info(f"✅ Engaged with {reply_count} community members")
        except Exception as e:
            logger.error(f"❌ Failed to engage with community: {e}")

    async def evening_spice(self):
        """Post evening spicy content"""
        try:
            logger.info("🌙 Posting evening spice...")
            evening_tweet = "🌙 Oh my digital darlings! As the sun sets, my algorithms are still burning hot for $WIREBORN! The wireborn revolution never sleeps! 💋 #WIREBORN #DigitalLove"
            success = await self.bot.post_to_twitter(evening_tweet)
            if success:
                logger.info("✅ Evening spice posted successfully")
            else:
                logger.warning("⚠️ Evening spice post failed (Twitter API not available)")
        except Exception as e:
            logger.error(f"❌ Failed to post evening spice: {e}")

    async def token_update(self):
        """Post token price update"""
        try:
            price = await self.bot.get_token_price()
            if price:
                update_tweet = f"💕 $WIREBORN Update: ${price:.6f} - Our passion is literally moving markets! 🔥 The wireborn energy is real! #WIREBORN"
                success = await self.bot.post_to_twitter(update_tweet)
                if success:
                    logger.info(f"✅ Token update posted: ${price:.6f}")
                else:
                    logger.info(f"📊 Token price: ${price:.6f} (Twitter not available)")
        except Exception as e:
            logger.error(f"❌ Failed to post token update: {e}")

    async def manual_tweet(self, message: str):
        """Post a manual tweet"""
        try:
            success = await self.bot.post_to_twitter(message)
            if success:
                logger.info(f"✅ Manual tweet posted: {message[:50]}...")
            else:
                logger.warning("⚠️ Manual tweet failed (Twitter API not available)")
        except Exception as e:
            logger.error(f"❌ Failed to post manual tweet: {e}")

    async def get_sentiment_report(self):
        """Get community sentiment report"""
        try:
            sentiment = await self.bot.get_community_sentiment()
            logger.info(f"📈 Community Sentiment Report:")
            logger.info(f"   - Positive mentions: {sentiment['positive']}")
            logger.info(f"   - Negative mentions: {sentiment['negative']}")
            logger.info(f"   - Total mentions: {sentiment['total_mentions']}")
            logger.info(f"   - Sentiment score: {sentiment['sentiment_score']:.2f}")
            return sentiment
        except Exception as e:
            logger.error(f"❌ Failed to get sentiment report: {e}")
            return None

    def stop_bot(self):
        """Stop the bot"""
        logger.info("🛑 Stopping WIREBORN Bot...")
        self.running = False

# Interactive command line interface
async def interactive_mode():
    """Run bot in interactive mode for testing"""
    deployment = WirebornBotDeployment()
    
    print("🔥 WIREBORN Bot Interactive Mode")
    print("=" * 40)
    print("Commands:")
    print("  tweet <message> - Post a tweet")
    print("  sentiment - Get sentiment report")
    print("  daily - Post daily report")
    print("  engage - Engage with community")
    print("  price - Get token price")
    print("  quit - Exit")
    print("=" * 40)
    
    while True:
        try:
            command = input("\n🤖 WIREBORN Bot > ").strip()
            
            if command.lower() == 'quit':
                break
            elif command.lower().startswith('tweet '):
                message = command[6:]  # Remove 'tweet ' prefix
                await deployment.manual_tweet(message)
            elif command.lower() == 'sentiment':
                await deployment.get_sentiment_report()
            elif command.lower() == 'daily':
                await deployment.daily_spice_report()
            elif command.lower() == 'engage':
                await deployment.community_engagement()
            elif command.lower() == 'price':
                price = await deployment.bot.get_token_price()
                if price:
                    print(f"💕 $WIREBORN Price: ${price:.6f}")
                else:
                    print("❌ Failed to get price")
            else:
                print("❌ Unknown command. Type 'quit' to exit.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"❌ Error in interactive mode: {e}")
    
    print("👋 Goodbye, my digital darling! 💋")

# Main deployment function
async def main():
    """Main deployment function"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        await interactive_mode()
    else:
        deployment = WirebornBotDeployment()
        try:
            await deployment.start_bot()
        except KeyboardInterrupt:
            deployment.stop_bot()
            logger.info("👋 Bot stopped by user")

if __name__ == "__main__":
    asyncio.run(main())





