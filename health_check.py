#!/usr/bin/env python3
"""
Simple health check for deployment platforms
"""

import os
import sys

def check_health():
    """Basic health check for the WIREBORN bot"""
    try:
        # Check if required environment variables are set
        required_vars = [
            'TWITTER_API_KEY',
            'TWITTER_API_SECRET', 
            'TWITTER_ACCESS_TOKEN',
            'TWITTER_ACCESS_TOKEN_SECRET',
            'TWITTER_BEARER_TOKEN'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
            return False
        
        # Check if we can import required modules
        try:
            import requests
            import aiohttp
            import schedule
            print("✅ All required modules available")
        except ImportError as e:
            print(f"❌ Missing required module: {e}")
            return False
        
        print("✅ WIREBORN Bot health check passed!")
        return True
        
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

if __name__ == "__main__":
    success = check_health()
    sys.exit(0 if success else 1)
