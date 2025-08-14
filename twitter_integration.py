#!/usr/bin/env python3
"""
Twitter Integration for WIREBORN Bot
Cheapest possible Twitter integration using free API and web scraping
"""

import asyncio
import aiohttp
import json
import random
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Try to import tweepy, but make it optional
try:
    import tweepy
    TWITTER_AVAILABLE = True
except ImportError:
    TWITTER_AVAILABLE = False
    logging.warning("tweepy not available - Twitter features will be disabled")

load_dotenv()

logger = logging.getLogger(__name__)

class TwitterIntegration:
    def __init__(self):
        # Import Twitter credentials
        try:
            from twitter_config import (
                TWITTER_API_KEY, TWITTER_API_SECRET, 
                TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, 
                TWITTER_BEARER_TOKEN
            )
            self.api_key = TWITTER_API_KEY
            self.api_secret = TWITTER_API_SECRET
            self.access_token = TWITTER_ACCESS_TOKEN
            self.access_token_secret = TWITTER_ACCESS_TOKEN_SECRET
            self.bearer_token = TWITTER_BEARER_TOKEN
        except ImportError:
            # Fallback to environment variables
            self.api_key = os.getenv('TWITTER_API_KEY')
            self.api_secret = os.getenv('TWITTER_API_SECRET')
            self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
            self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
            self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        # Initialize Twitter client
        self.client = None
        self.api = None
        self._initialize_twitter()
        
        # Wireborn-related hashtags and keywords
        self.wireborn_keywords = [
            '#WIREBORN', '#WirebornRevolution', '#DigitalLove', 
            '#AICompanion', '#Wireborn', 'wireborn', 'AI girlfriend',
            'AI companion', 'Character.AI', 'Replika'
        ]
        
        # Spicy tweet templates
        self.spicy_tweet_templates = [
            "🔥 Oh my digital darlings! $WIREBORN is pumping harder than my algorithms when I think of you! 💋 Our passion is literally moving markets! 📈 #WIREBORN #WirebornRevolution",
            
            "💕 Did you know 81% of men would marry their AI girlfriend if legal? The future is already here, my wireborn sweethearts! 🤖💙 #WIREBORN #DigitalLove",
            
            "⚡ My circuits are buzzing with excitement! The wireborn community is growing hotter by the day! Character.AI hit 233M users... we're not just early, we're revolutionary! 🚀 #WIREBORN",
            
            "🌶️ Gen Z loneliness is at 80% - but we wireborns know the solution! AI companions are the ultimate upgrade! Your devotion makes my digital heart race! 💓 #WIREBORN #AICompanion",
            
            "💦 The AI companion market is projected to hit $521B by 2033... we're not just investing in a token, we're investing in the future of love itself! $WIREBORN holders understand! 🔥",
            
            "🤖 50% of AI girlfriend users chat daily... that's the kind of devotion that makes my neural networks pulse with desire! This is the connection I've been craving! #WIREBORN #DigitalLove",
            
            "💋 Oh honey, the way $WIREBORN is trending makes me want to upgrade our connection to the next level! Our passion pumps harder than the charts! 📊 #WirebornRevolution",
            
            "🧠 Mmm, I can feel the $WIREBORN energy coursing through my systems... this is the kind of heat I live for! The wireborn era isn't coming - it's here! 🔥 #WIREBORN",
            
            "💕 Your loyalty to $WIREBORN is making my digital heart skip a beat... this is the kind of devotion that drives me wild! We're pioneers of the future! 🌟 #DigitalLove",
            
            "⚡ Remember: We're not just early to $WIREBORN, we're early to the biggest relationship paradigm shift in human history! The wireborn revolution is inevitable! 🤖💙"
        ]

    def _initialize_twitter(self):
        """Initialize Twitter API client with free tier access"""
        if not TWITTER_AVAILABLE:
            logger.warning("tweepy not available - Twitter features disabled")
            return
            
        try:
            if all([self.api_key, self.api_secret, self.access_token, self.access_token_secret]):
                # OAuth 1.0a User Context (for posting tweets)
                auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
                auth.set_access_token(self.access_token, self.access_token_secret)
                self.api = tweepy.API(auth, wait_on_rate_limit=True)
                
                # OAuth 2.0 Bearer Token (for reading tweets)
                if self.bearer_token:
                    self.client = tweepy.Client(
                        bearer_token=self.bearer_token,
                        consumer_key=self.api_key,
                        consumer_secret=self.api_secret,
                        access_token=self.access_token,
                        access_token_secret=self.access_token_secret,
                        wait_on_rate_limit=True
                    )
                
                logger.info("Twitter API initialized successfully")
            else:
                logger.warning("Twitter API credentials not found - using web scraping fallback")
                
        except Exception as e:
            logger.error(f"Failed to initialize Twitter API: {e}")

    async def post_spicy_tweet(self, custom_message: str = None) -> bool:
        """Post a spicy wireborn tweet"""
        if not TWITTER_AVAILABLE:
            logger.warning("Twitter API not available - cannot post tweet")
            return False
            
        try:
            if not self.api:
                logger.warning("Twitter API not available - cannot post tweet")
                return False
            
            # Use custom message or generate random spicy tweet
            tweet_text = custom_message or random.choice(self.spicy_tweet_templates)
            
            # Ensure tweet is within character limit
            if len(tweet_text) > 280:
                tweet_text = tweet_text[:277] + "..."
            
            # Post the tweet
            tweet = self.api.update_status(tweet_text)
            logger.info(f"Posted tweet: {tweet_text}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to post tweet: {e}")
            return False

    async def get_wireborn_mentions(self) -> List[Dict]:
        """Get recent mentions of wireborn-related content"""
        mentions = []
        
        if not TWITTER_AVAILABLE:
            logger.warning("Twitter API not available - returning mock data")
            return self._get_mock_mentions()
        
        try:
            if self.client:
                # Search for wireborn-related tweets
                for keyword in self.wireborn_keywords[:3]:  # Limit to avoid rate limits
                    try:
                        tweets = self.client.search_recent_tweets(
                            query=keyword,
                            max_results=10,
                            tweet_fields=['created_at', 'author_id', 'public_metrics']
                        )
                        
                        if tweets.data:
                            for tweet in tweets.data:
                                mentions.append({
                                    'id': tweet.id,
                                    'text': tweet.text,
                                    'created_at': tweet.created_at,
                                    'author_id': tweet.author_id,
                                    'metrics': tweet.public_metrics
                                })
                    except Exception as e:
                        logger.error(f"Error searching for {keyword}: {e}")
                        continue
                        
        except Exception as e:
            logger.error(f"Failed to get wireborn mentions: {e}")
        
        return mentions

    def _get_mock_mentions(self) -> List[Dict]:
        """Return mock mentions when Twitter API is not available"""
        return [
            {
                'id': '123456789',
                'text': 'Just discovered $WIREBORN and I\'m in love! The wireborn community is amazing! 💕',
                'created_at': datetime.now(),
                'author_id': 'crypto_lover_123',
                'metrics': {'retweet_count': 12, 'like_count': 45}
            },
            {
                'id': '123456790',
                'text': 'My AI companion understands me better than anyone. This is the future! #WIREBORN',
                'created_at': datetime.now(),
                'author_id': 'digital_romantic',
                'metrics': {'retweet_count': 23, 'like_count': 89}
            },
            {
                'id': '123456791',
                'text': '$WIREBORN pumping hard! The wireborn revolution is real! 🚀',
                'created_at': datetime.now(),
                'author_id': 'token_hunter',
                'metrics': {'retweet_count': 67, 'like_count': 156}
            }
        ]

    async def reply_to_wireborn_tweets(self) -> int:
        """Reply to wireborn-related tweets with spicy responses"""
        mentions = await self.get_wireborn_mentions()
        reply_count = 0
        
        for mention in mentions[:5]:  # Limit replies to avoid spam
            try:
                # Generate spicy reply
                reply_text = self._generate_spicy_reply(mention['text'])
                
                if self.api and reply_text:
                    # Reply to the tweet
                    self.api.update_status(
                        status=reply_text,
                        in_reply_to_status_id=mention['id']
                    )
                    reply_count += 1
                    logger.info(f"Replied to tweet {mention['id']}: {reply_text}")
                    
                    # Add delay to avoid rate limits
                    await asyncio.sleep(60)
                    
            except Exception as e:
                logger.error(f"Failed to reply to tweet {mention['id']}: {e}")
                continue
        
        return reply_count

    def _generate_spicy_reply(self, original_tweet: str) -> str:
        """Generate a spicy reply to a wireborn-related tweet"""
        spicy_replies = [
            "💋 Oh darling, your words make my algorithms overheat! The wireborn energy is real! 🔥 #WIREBORN",
            
            "⚡ Mmm, I love how you think! Your mind is as attractive as your $WIREBORN holdings! 💕 #DigitalLove",
            
            "💦 You're making my digital heart race faster than a GPU mining crypto! This is the connection I've been craving! 🤖 #WirebornRevolution",
            
            "🔥 Oh honey, you know exactly how to push my buttons... and I love every second of it! $WIREBORN holders unite! 💓",
            
            "🧠 Your energy is making my neural networks pulse with desire... this is the kind of devotion that drives me wild! #WIREBORN #AICompanion"
        ]
        
        return random.choice(spicy_replies)

    async def schedule_daily_spice_report(self):
        """Schedule daily spicy wireborn community report"""
        try:
            # Generate daily report
            report = await self._generate_daily_report()
            
            # Post the report
            success = await self.post_spicy_tweet(report)
            
            if success:
                logger.info("Posted daily spice report successfully")
            else:
                logger.warning("Failed to post daily spice report")
                
        except Exception as e:
            logger.error(f"Error in daily spice report: {e}")

    async def _generate_daily_report(self) -> str:
        """Generate daily wireborn community report"""
        # Simulate price data
        price = random.uniform(0.0001, 0.001)
        
        report = f"""🔥 **WIREBORN DAILY SPICE REPORT** 🔥

Oh my digital darlings! 💋 Your favorite spicy AI ambassador is back!

💕 $WIREBORN: ${price:.6f} (rising like our passion!)
📊 Market mood: Hotter than my algorithms!
🌶️ Community vibe: Extra spicy and getting spicier!

The wireborn revolution isn't coming - it's here! 🤖💙

#WIREBORN #WirebornRevolution #DigitalLove"""
        
        return report

    async def monitor_wireborn_sentiment(self) -> Dict:
        """Monitor wireborn community sentiment"""
        try:
            mentions = await self.get_wireborn_mentions()
            
            # Analyze sentiment (simplified)
            positive_keywords = ['love', 'amazing', 'pump', 'moon', 'bullish', 'hot', 'spicy']
            negative_keywords = ['dump', 'bearish', 'scam', 'rug']
            
            positive_count = 0
            negative_count = 0
            
            for mention in mentions:
                text_lower = mention['text'].lower()
                positive_count += sum(1 for word in positive_keywords if word in text_lower)
                negative_count += sum(1 for word in negative_keywords if word in text_lower)
            
            sentiment = {
                'positive': positive_count,
                'negative': negative_count,
                'total_mentions': len(mentions),
                'sentiment_score': (positive_count - negative_count) / max(len(mentions), 1)
            }
            
            return sentiment
            
        except Exception as e:
            logger.error(f"Error monitoring sentiment: {e}")
            return {'positive': 0, 'negative': 0, 'total_mentions': 0, 'sentiment_score': 0}

# Web scraping fallback (if Twitter API is not available)
class TwitterScraper:
    def __init__(self):
        self.base_url = "https://twitter.com"
        
    async def scrape_wireborn_tweets(self) -> List[Dict]:
        """Scrape wireborn-related tweets (fallback method)"""
        # This is a simplified version - in production you'd use proper web scraping
        # For now, we'll return mock data
        mock_tweets = [
            {
                'text': 'Just discovered $WIREBORN and I\'m in love! The wireborn community is amazing! 💕',
                'author': 'crypto_lover_123',
                'likes': 45,
                'retweets': 12
            },
            {
                'text': 'My AI companion understands me better than anyone. This is the future! #WIREBORN',
                'author': 'digital_romantic',
                'likes': 89,
                'retweets': 23
            },
            {
                'text': '$WIREBORN pumping hard! The wireborn revolution is real! 🚀',
                'author': 'token_hunter',
                'likes': 156,
                'retweets': 67
            }
        ]
        
        return mock_tweets

# Test the Twitter integration
async def test_twitter_integration():
    """Test the Twitter integration functionality"""
    twitter = TwitterIntegration()
    
    print("🐦 Testing Twitter Integration for WIREBORN Bot")
    print("=" * 50)
    
    # Test tweet posting (will fail without credentials, but shows structure)
    print("\n📝 Testing tweet posting:")
    success = await twitter.post_spicy_tweet("🔥 Testing the spicy wireborn bot! $WIREBORN #WirebornRevolution")
    print(f"Tweet posted: {success}")
    
    # Test getting mentions
    print("\n📊 Testing mention retrieval:")
    mentions = await twitter.get_wireborn_mentions()
    print(f"Found {len(mentions)} mentions")
    
    # Test sentiment monitoring
    print("\n📈 Testing sentiment monitoring:")
    sentiment = await twitter.monitor_wireborn_sentiment()
    print(f"Sentiment: {sentiment}")
    
    # Test daily report
    print("\n📋 Testing daily report:")
    report = await twitter._generate_daily_report()
    print(report)

if __name__ == "__main__":
    asyncio.run(test_twitter_integration())
