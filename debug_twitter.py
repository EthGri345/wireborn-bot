#!/usr/bin/env python3
"""
Debug Twitter Authentication
More detailed debugging for Twitter API issues
"""

import requests
from requests_oauthlib import OAuth1Session
import json

def debug_twitter():
    """Debug Twitter authentication with more details"""
    
    # Twitter API credentials
    api_key = "0NhNTyeuhNx2ZXuiZysIvaVULEQVIPrMvMFzkbZaL0gwlt9e2T"
    api_secret = "FpoQqrF2j3xrRFaScuYhL9Lg9"
    access_token = "1955794179663257603-q2nr0ijFv3difvf6auNM41VMA05l1R"
    access_token_secret = "37wHCRBxQLqgfcnSEE5QPAi8TR85hHC3aNp1b8OQbBqoY"
    
    print("🔍 Debugging Twitter Authentication")
    print("=" * 50)
    
    print(f"API Key: {api_key[:10]}...{api_key[-10:]}")
    print(f"API Secret: {api_secret[:10]}...{api_secret[-10:]}")
    print(f"Access Token: {access_token[:10]}...{access_token[-10:]}")
    print(f"Access Token Secret: {access_token_secret[:10]}...{access_token_secret[-10:]}")
    
    # Test 1: Check if credentials are valid format
    print("\n1. Checking credential formats:")
    print(f"API Key length: {len(api_key)} (should be ~25)")
    print(f"API Secret length: {len(api_secret)} (should be ~50)")
    print(f"Access Token length: {len(access_token)} (should be ~50)")
    print(f"Access Token Secret length: {len(access_token_secret)} (should be ~50)")
    
    # Test 2: Try a simpler OAuth test
    print("\n2. Testing OAuth with different endpoint:")
    try:
        oauth = OAuth1Session(
            api_key,
            client_secret=api_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )
        
        # Try a different endpoint
        url = "https://api.twitter.com/1.1/help/configuration.json"
        response = oauth.get(url)
        print(f"Configuration endpoint status: {response.status_code}")
        if response.status_code == 200:
            print("✅ OAuth is working!")
        else:
            print(f"❌ OAuth failed: {response.text}")
            
    except Exception as e:
        print(f"❌ OAuth error: {e}")
    
    # Test 3: Try with different OAuth library
    print("\n3. Testing with different OAuth approach:")
    try:
        import oauth2 as oauth
        
        consumer = oauth.Consumer(api_key, api_secret)
        token = oauth.Token(access_token, access_token_secret)
        client = oauth.Client(consumer, token)
        
        url = "https://api.twitter.com/1.1/account/verify_credentials.json"
        response, content = client.request(url)
        print(f"OAuth2 status: {response['status']}")
        if response['status'] == '200':
            print("✅ OAuth2 is working!")
        else:
            print(f"❌ OAuth2 failed: {content}")
            
    except ImportError:
        print("❌ oauth2 library not available")
    except Exception as e:
        print(f"❌ OAuth2 error: {e}")
    
    print("\n" + "=" * 50)
    print("🔧 Troubleshooting Steps:")
    print("1. Go to Twitter Developer Portal")
    print("2. Check if your app is in 'Development' mode")
    print("3. Verify all credentials are copied correctly")
    print("4. Try regenerating access tokens manually")
    print("5. Check if your app has the correct permissions")

if __name__ == "__main__":
    debug_twitter()
