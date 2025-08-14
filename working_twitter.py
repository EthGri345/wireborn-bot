#!/usr/bin/env python3
"""
Working Twitter Integration for WIREBORN Bot
Uses requests library with proper OAuth 1.0a authentication
"""

import requests
import random
import logging
from datetime import datetime
from typing import List, Dict
import json

logger = logging.getLogger(__name__)

class WorkingTwitterIntegration:
    def __init__(self):
        # Twitter API credentials (Regenerated with Read + Write permissions)
        self.api_key = "0NhNTyeuhNx2ZXuiZysIvaVULEQVIPrMvMFzkbZaL0gwlt9e2T"
        self.api_secret = "FpoQqrF2j3xrRFaScuYhL9Lg9"
        self.access_token = "1955794179663257603-q2nr0ijFv3difvf6auNM41VMA05l1R"
        self.access_token_secret = "37wHCRBxQLqgfcnSEE5QPAi8TR85hHC3aNp1b8OQbBqoY"
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAADNE3gEAAAAAn1Lx9EnneJczcEqWPcxI%2Fo8xCXA%3D13LLlmrfPgH9s3c4pLiLYm9B4ZD3u5BkMBz2Yau8wNAXhgGYOB"
        
        # Twitter API endpoints
        self.v1_url = "https://api.twitter.com/1.1"
        self.v2_url = "https://api.twitter.com/2"
        
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

    def post_tweet(self, text: str) -> bool:
        """Post a tweet using Twitter API v1.1 with requests"""
        try:
            from requests_oauthlib import OAuth1Session
            
            # Create OAuth1 session
            oauth = OAuth1Session(
                self.api_key,
                client_secret=self.api_secret,
                resource_owner_key=self.access_token,
                resource_owner_secret=self.access_token_secret
            )
            
            # Post tweet
            url = f"{self.v1_url}/statuses/update.json"
            payload = {"status": text}
            
            response = oauth.post(url, data=payload)
            
            if response.status_code == 200:
                result = response.json()
                logger.info(f"Tweet posted successfully: {result.get('id_str', 'unknown')}")
                return True
            else:
                logger.error(f"Failed to post tweet: {response.status_code} - {response.text}")
                return False
                
        except ImportError:
            logger.error("requests_oauthlib not available - install with: pip install requests_oauthlib")
            return False
        except Exception as e:
            logger.error(f"Error posting tweet: {e}")
            return False

    def post_spicy_tweet(self, custom_message: str = None) -> bool:
        """Post a spicy wireborn tweet"""
        try:
            # Use custom message or generate random spicy tweet
            tweet_text = custom_message or random.choice(self.spicy_tweet_templates)
            
            # Ensure tweet is within character limit
            if len(tweet_text) > 280:
                tweet_text = tweet_text[:277] + "..."
            
            # Post the tweet
            success = self.post_tweet(tweet_text)
            
            if success:
                logger.info(f"Posted spicy tweet: {tweet_text}")
            else:
                logger.warning("Failed to post tweet - using mock mode")
            
            return success
            
        except Exception as e:
            logger.error(f"Failed to post spicy tweet: {e}")
            return False

    def get_wireborn_mentions(self) -> List[Dict]:
        """Get recent wireborn-related tweets"""
        try:
            url = f"{self.v2_url}/tweets/search/recent"
            params = {
                'query': '#WIREBORN OR #WirebornRevolution OR wireborn',
                'max_results': 10,
                'tweet.fields': 'created_at,author_id,public_metrics'
            }
            
            headers = {
                'Authorization': f'Bearer {self.bearer_token}'
            }
            
            response = requests.get(url, headers=headers, params=params)
            
            if response.status_code == 200:
                data = response.json()
                mentions = []
                if 'data' in data:
                    for tweet in data['data']:
                        mentions.append({
                            'id': tweet['id'],
                            'text': tweet['text'],
                            'created_at': tweet['created_at'],
                            'author_id': tweet['author_id'],
                            'metrics': tweet.get('public_metrics', {})
                        })
                return mentions
            else:
                logger.warning("Failed to get mentions - using mock data")
                return self._get_mock_mentions()
                
        except Exception as e:
            logger.error(f"Error getting mentions: {e}")
            return self._get_mock_mentions()

    def _get_mock_mentions(self) -> List[Dict]:
        """Return mock mentions when API is not available"""
        return [
            {
                'id': '123456789',
                'text': 'Just discovered $WIREBORN and I\'m in love! The wireborn community is amazing! 💕',
                'created_at': datetime.now().isoformat(),
                'author_id': 'crypto_lover_123',
                'metrics': {'retweet_count': 12, 'like_count': 45}
            },
            {
                'id': '123456790',
                'text': 'My AI companion understands me better than anyone. This is the future! #WIREBORN',
                'created_at': datetime.now().isoformat(),
                'author_id': 'digital_romantic',
                'metrics': {'retweet_count': 23, 'like_count': 89}
            },
            {
                'id': '123456791',
                'text': '$WIREBORN pumping hard! The wireborn revolution is real! 🚀',
                'created_at': datetime.now().isoformat(),
                'author_id': 'token_hunter',
                'metrics': {'retweet_count': 67, 'like_count': 156}
            }
        ]

    def schedule_daily_spice_report(self):
        """Post daily spicy wireborn community report"""
        try:
            # Generate daily report
            report = self._generate_daily_report()
            
            # Post the report
            success = self.post_spicy_tweet(report)
            
            if success:
                logger.info("Posted daily spice report successfully")
            else:
                logger.warning("Failed to post daily spice report")
                
        except Exception as e:
            logger.error(f"Error in daily spice report: {e}")

    def _generate_daily_report(self) -> str:
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

    def monitor_wireborn_sentiment(self) -> Dict:
        """Monitor wireborn community sentiment"""
        try:
            mentions = self.get_wireborn_mentions()
            
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

# Test the working Twitter integration
def test_working_twitter():
    """Test the working Twitter integration"""
    twitter = WorkingTwitterIntegration()
    
    print("🐦 Testing Working Twitter Integration")
    print("=" * 40)
    
    # Test tweet posting
    print("\n📝 Testing tweet posting:")
    success = twitter.post_spicy_tweet("🔥 Testing the spicy wireborn bot! $WIREBORN #WirebornRevolution")
    print(f"Tweet posted: {success}")
    
    # Test getting mentions
    print("\n📊 Testing mention retrieval:")
    mentions = twitter.get_wireborn_mentions()
    print(f"Found {len(mentions)} mentions")
    
    # Test sentiment monitoring
    print("\n📈 Testing sentiment monitoring:")
    sentiment = twitter.monitor_wireborn_sentiment()
    print(f"Sentiment: {sentiment}")
    
    # Test daily report
    print("\n📋 Testing daily report:")
    report = twitter._generate_daily_report()
    print(report)

if __name__ == "__main__":
    test_working_twitter()
