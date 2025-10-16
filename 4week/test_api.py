#!/usr/bin/env python3
"""
Script untuk testing API Flask SQLAlchemy
"""

import requests
import json
import time

API_BASE = "http://localhost:5000"

def test_api():
    print("🚀 Testing Flask SQLAlchemy API")
    print("=" * 50)
    
    # Test 1: Get API info
    print("\n1. Testing API Info...")
    try:
        response = requests.get(f"{API_BASE}/api")
        print(f"✅ Status: {response.status_code}")
        print(f"📄 Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Get all users (should be empty initially)
    print("\n2. Testing GET /users...")
    try:
        response = requests.get(f"{API_BASE}/users")
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"👥 Users count: {data.get('total', 0)}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Create a user
    print("\n3. Testing POST /users...")
    test_user = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    try:
        response = requests.post(f"{API_BASE}/users", json=test_user)
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"📄 Response: {data}")
        user_id = data.get('user', {}).get('id')
    except Exception as e:
        print(f"❌ Error: {e}")
        user_id = None
    
    # Test 4: Create another user
    print("\n4. Testing POST /users (second user)...")
    test_user2 = {
        "name": "Jane Smith",
        "email": "jane@example.com"
    }
    try:
        response = requests.post(f"{API_BASE}/users", json=test_user2)
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"📄 Response: {data}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 5: Get all users (should have 2 users now)
    print("\n5. Testing GET /users (after creating users)...")
    try:
        response = requests.get(f"{API_BASE}/users")
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"👥 Users count: {data.get('total', 0)}")
        for user in data.get('users', []):
            print(f"   - {user['name']} ({user['email']})")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 6: Get specific user
    if user_id:
        print(f"\n6. Testing GET /users/{user_id}...")
        try:
            response = requests.get(f"{API_BASE}/users/{user_id}")
            print(f"✅ Status: {response.status_code}")
            data = response.json()
            print(f"📄 Response: {data}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Test 7: Update user
    if user_id:
        print(f"\n7. Testing PUT /users/{user_id}...")
        update_data = {
            "name": "John Updated",
            "email": "john.updated@example.com"
        }
        try:
            response = requests.put(f"{API_BASE}/users/{user_id}", json=update_data)
            print(f"✅ Status: {response.status_code}")
            data = response.json()
            print(f"📄 Response: {data}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Test 8: Try to create duplicate email
    print("\n8. Testing POST /users (duplicate email)...")
    duplicate_user = {
        "name": "Duplicate User",
        "email": "john@example.com"  # Same email as first user
    }
    try:
        response = requests.post(f"{API_BASE}/users", json=duplicate_user)
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"📄 Response: {data}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 9: Delete user
    if user_id:
        print(f"\n9. Testing DELETE /users/{user_id}...")
        try:
            response = requests.delete(f"{API_BASE}/users/{user_id}")
            print(f"✅ Status: {response.status_code}")
            data = response.json()
            print(f"📄 Response: {data}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Test 10: Final check - get all users
    print("\n10. Final check - GET /users...")
    try:
        response = requests.get(f"{API_BASE}/users")
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"👥 Final users count: {data.get('total', 0)}")
        for user in data.get('users', []):
            print(f"   - {user['name']} ({user['email']})")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API Testing Complete!")

if __name__ == "__main__":
    print("Make sure Flask app is running on http://localhost:5000")
    print("Press Enter to start testing...")
    input()
    test_api()
