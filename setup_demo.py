#!/usr/bin/env python3
"""
Demo setup script for Tamil AI Extension
"""
import os
import subprocess
import sys

def create_env_file():
    """Create .env file with API key"""
    env_path = "backend/.env"
    
    if os.path.exists(env_path):
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file...")
    
    api_key = input("Enter your Gemini API key: ").strip()
    
    if not api_key:
        print("❌ API key is required")
        return False
    
    try:
        with open(env_path, 'w') as f:
            f.write(f"GEMINI_API_KEY={api_key}\n")
        
        print("✅ .env file created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def check_backend_running():
    """Check if backend is running"""
    try:
        import requests
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def start_backend():
    """Start the backend server"""
    print("🚀 Starting backend server...")
    
    try:
        # Change to backend directory and start the server
        os.chdir("backend")
        subprocess.Popen([sys.executable, "app.py"], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
        
        print("✅ Backend server started")
        print("🌐 Server running at: http://localhost:8000")
        return True
        
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return False

def main():
    print("🎯 Tamil AI Demo Setup")
    print("=" * 30)
    
    # Step 1: Create .env file
    if not create_env_file():
        return
    
    # Step 2: Check if backend is running
    if check_backend_running():
        print("✅ Backend is already running")
    else:
        print("🔄 Backend not running, starting it...")
        if not start_backend():
            return
    
    # Step 3: Run tests
    print("\n🧪 Running API tests...")
    try:
        result = subprocess.run([sys.executable, "test_gemini_api.py"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"❌ Error running tests: {e}")
    
    print("\n📋 Demo Setup Complete!")
    print("=" * 30)
    print("✅ Backend server: http://localhost:8000")
    print("✅ Extension ready for testing")
    print("\n🎯 Demo Instructions:")
    print("1. Reload your Chrome extension")
    print("2. Select Tamil text on any webpage")
    print("3. Right-click → Tamil AI Assistant → Grammar Check")
    print("4. See the results in the chat panel!")

if __name__ == "__main__":
    main()

