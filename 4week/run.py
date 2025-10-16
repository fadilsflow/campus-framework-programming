#!/usr/bin/env python3
"""
Script untuk menjalankan Flask aplikasi dengan setup otomatis
"""

import subprocess
import sys
import os
import time

def install_requirements():
    """Install requirements jika belum terinstall"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def check_database():
    """Check if database connection is working"""
    print("🔍 Checking database connection...")
    try:
        from main import app, db
        with app.app_context():
            db.create_all()
            print("✅ Database connection successful!")
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("💡 Make sure MySQL is running and database 'flask-week-4' exists")
        return False

def run_app():
    """Run the Flask application"""
    print("🚀 Starting Flask application...")
    print("🌐 Frontend: http://localhost:5000")
    print("🔧 API Info: http://localhost:5000/api")
    print("📊 Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def main():
    print("🎯 Flask SQLAlchemy CRUD Application")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("main.py"):
        print("❌ main.py not found. Make sure you're in the project directory.")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check database
    if not check_database():
        print("\n💡 To fix database issues:")
        print("1. Make sure MySQL is running")
        print("2. Create database: CREATE DATABASE `flask-week-4`;")
        print("3. Check your MySQL credentials in main.py")
        return
    
    # Run application
    run_app()

if __name__ == "__main__":
    main()
