#!/usr/bin/env python3
"""
Test Twitter Authentication
Simple test to diagnose Twitter API authentication issues
"""

import requests
from requests_oauthlib import OAuth1Session
import json

def test_twitter_auth():
    """Test Twitter authentication with detailed error reporting"""
    
    # Twitter API credentials
    api_key = "0NhNTyeuhNx2ZXuiZysIvaVULEQVIPrMvMFzkbZaL0gwlt9e2T"
    api_secret = "FpoQqrF2j3xrRFaScuYhL9Lg9"
    access_token = "1955794179663257603-q2nr0ijFv3difvf6auNM41VMA05l1R"
    access_token_secret = "37wHCRBxQLqgfcnSEE5QPAi8TR85hHC3aNp1b8OQbBqoY"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAADNE3gEAAAAAn1Lx9EnneJczcEqWPcxI%2Fo8xCXA%3D13LLlmrfPgH9s3c4pLiLYm9B4ZD3u5BkMBz2Yau8wNAXhgGYOB"
    
    print("🐦 Testing Twitter Authentication")
    print("=" * 40)
    
    # Test 1: Bearer token (for reading tweets)
    print("\n1. Testing Bearer Token (Read Access):")
    try:
        url = "https://api.twitter.com/2/users/me"
        headers = {'Authorization': f'Bearer {bearer_token}'}
        response = requests.get(url, headers=headers)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Bearer token works! User: {data.get('data', {}).get('username', 'unknown')}")
        else:
            print(f"❌ Bearer token failed: {response.text}")
    except Exception as e:
        print(f"❌ Bearer token error: {e}")
    
    # Test 2: OAuth 1.0a (for posting tweets)
    print("\n2. Testing OAuth 1.0a (Write Access):")
    try:
        oauth = OAuth1Session(
            api_key,
            client_secret=api_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )
        
        # Test with a simple endpoint first
        url = "https://api.twitter.com/1.1/account/verify_credentials.json"
        response = oauth.get(url)
        print(f"Credentials verification status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ OAuth 1.0a works! User: @{data.get('screen_name', 'unknown')}")
        else:
            print(f"❌ OAuth 1.0a failed: {response.text}")
            
    except Exception as e:
        print(f"❌ OAuth 1.0a error: {e}")
    
    # Test 3: Try to post a tweet
    print("\n3. Testing Tweet Posting:")
    try:
        test_tweet = "🔥 Testing the spicy wireborn bot! $WIREBORN #WirebornRevolution"
        url = "https://api.twitter.com/1.1/statuses/update.json"
        payload = {"status": test_tweet}
        
        response = oauth.post(url, data=payload)
        print(f"Tweet posting status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Tweet posted successfully! ID: {data.get('id_str', 'unknown')}")
        else:
            print(f"❌ Tweet posting failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Tweet posting error: {e}")
    
    print("\n" + "=" * 40)
    print("🔧 Configuration Recommendations:")
    print("1. Check Twitter Developer Portal settings:")
    print("   - App permissions: Read + Write")
    print("   - Callback URL: http://127.0.0.1 (for testing)")
    print("   - Website URL: http://127.0.0.1 (for testing)")
    print("2. Verify API keys are correct")
    print("3. Ensure tokens have proper scopes")

if __name__ == "__main__":
    test_twitter_auth()
