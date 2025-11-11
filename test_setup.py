"""
Quick Test Script
Run this to verify everything works!
"""

import os
import sys

print("🧪 Running Quick Tests...\n")

# Test 1: Check Python version
print("1️⃣ Checking Python version...")
python_version = sys.version_info
if python_version.major >= 3 and python_version.minor >= 9:
    print(f"   ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
else:
    print(f"   ❌ Python {python_version.major}.{python_version.minor} is too old. Need 3.9+")
    sys.exit(1)

# Test 2: Check dependencies
print("\n2️⃣ Checking dependencies...")
try:
    import whisper
    print("   ✅ openai-whisper installed")
except ImportError:
    print("   ❌ openai-whisper not found. Run: pip install -r requirements.txt")
    sys.exit(1)

try:
    import requests
    print("   ✅ requests installed")
except ImportError:
    print("   ❌ requests not found")
    sys.exit(1)

try:
    from docx import Document
    print("   ✅ python-docx installed")
except ImportError:
    print("   ❌ python-docx not found")
    sys.exit(1)

# Test 3: Check .env file
print("\n3️⃣ Checking configuration...")
if not os.path.exists(".env"):
    print("   ❌ .env file not found!")
    print("      Copy .env.example to .env and add your API key")
    sys.exit(1)

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("   ❌ GOOGLE_API_KEY not set in .env file")
    sys.exit(1)
else:
    print(f"   ✅ API key configured: {api_key[:10]}...{api_key[-4:]}")

# Test 4: Check test videos
print("\n4️⃣ Checking test videos...")
test_videos = [f for f in os.listdir("test_videos") if f.endswith(".mp4")]
if test_videos:
    print(f"   ✅ Found {len(test_videos)} test videos:")
    for video in sorted(test_videos):
        size_mb = os.path.getsize(f"test_videos/{video}") / 1024 / 1024
        print(f"      - {video} ({size_mb:.1f} MB)")
else:
    print("   ⚠️  No test videos found")

# Test 5: Check outputs folder
print("\n5️⃣ Checking outputs folder...")
if not os.path.exists("outputs"):
    os.makedirs("outputs")
    print("   ✅ Created outputs/ folder")
else:
    print("   ✅ outputs/ folder exists")

print("\n" + "=" * 60)
print("✅ All basic checks passed!")
print("=" * 60)
print("\n📝 Next step: Process a test video")
print("   Run: python process_video.py test_videos/test_video_3.mp4")
print("\n💡 This will take 2-3 minutes and test the full pipeline:")
print("   1. Audio extraction")
print("   2. Whisper transcription")
print("   3. Google Gemini analysis")
print("   4. Document generation")
print("\n🎯 If that works, you're all set!")
print("=" * 60)
