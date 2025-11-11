# 🍎 Quick Start Guide for Mac Users

**For your friend who just cloned this repo on their Mac**

---

## ⚡ Super Fast Setup (5 Minutes)

### Step 1: Open Terminal
Press `Cmd + Space`, type "Terminal", press Enter

### Step 2: Navigate to the Project
```bash
cd ~/Downloads/AI-model  # or wherever you cloned it
```

### Step 3: Install Python Dependencies
```bash
pip3 install -r requirements.txt
```

**Wait 2-3 minutes** - This downloads all necessary libraries.

### Step 4: Get Your FREE Google Gemini API Key

1. Open this link: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (looks like: `AIzaSy...`)

### Step 5: Add Your API Key

```bash
# Open the .env file
nano .env

# You'll see:
# GOOGLE_API_KEY=AIzaSyDPMNX0GFFySpAScHYGPhnn1R4V_mvCSfw
#
# Replace the key with YOUR key
# Press Ctrl+X, then Y, then Enter to save
```

### Step 6: Test It!

```bash
python3 process_video.py test_videos/test_video_1.mp4
```

**Expected result:**
- Should take 2-3 minutes
- You'll see processing messages
- Files will be created in `outputs/` folder

### Step 7: Check Your Results

```bash
open outputs/
```

You should see:
- ✅ `test_video_1_analysis.docx` - Word document with summary & quiz
- ✅ `test_video_1_subtitles.srt` - Subtitle file

---

## 🎯 That's It!

Now you can process any video:

```bash
python3 process_video.py your_video.mp4
```

---

## 🔍 Common Mac Issues & Solutions

### Issue: "pip3: command not found"

**Solution 1 - Install Python:**
```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

**Solution 2 - Use python3 -m pip:**
```bash
python3 -m pip install -r requirements.txt
```

### Issue: "python3: command not found"

**Solution:**
```bash
# Install Python from Homebrew
brew install python3

# Or download from python.org
# Visit: https://www.python.org/downloads/macos/
```

### Issue: "SSL Certificate Error" when installing

**Solution:**
```bash
# Run the certificate installer
cd /Applications/Python\ 3.*/
./Install\ Certificates.command

# Or install with no-verify
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Issue: "Permission Denied"

**Solution:**
```bash
# Install for your user only (no sudo needed)
pip3 install --user -r requirements.txt
```

### Issue: "xcrun: error: invalid active developer path"

**Solution:**
```bash
# Install Xcode Command Line Tools
xcode-select --install
```

---

## 🍎 Mac M1/M2/M3 (Apple Silicon) Users

Great news! The script **automatically detects** your Apple Silicon chip and uses:
- **Metal GPU acceleration** for Whisper (super fast!)
- You'll see: "🚀 Using GPU acceleration (Apple Metal)"

No extra setup needed! 🎉

---

## 🧪 Test Videos Included

We included 6 test videos for you:

```bash
# Quick test (shortest video - 1 minute)
python3 process_video.py test_videos/test_video_1.mp4

# Try other videos
python3 process_video.py test_videos/test_video_2.mp4
python3 process_video.py test_videos/test_video_3.mp4
python3 process_video.py test_videos/test_video_4.mp4
python3 process_video.py test_videos/test_video_5.mp4
python3 process_video.py test_videos/test_video_6.mp4
```

---

## 📝 Step-by-Step Checklist

- [ ] 1. Open Terminal
- [ ] 2. Navigate to project: `cd ~/Downloads/AI-model`
- [ ] 3. Install dependencies: `pip3 install -r requirements.txt`
- [ ] 4. Get Google API key: https://makersuite.google.com/app/apikey
- [ ] 5. Edit .env file: `nano .env` (add your key)
- [ ] 6. Test: `python3 process_video.py test_videos/test_video_1.mp4`
- [ ] 7. Check outputs: `open outputs/`

---

## 🎬 Processing Your Own Videos

```bash
# From Downloads folder
python3 process_video.py ~/Downloads/my_lecture.mp4

# From Movies folder
python3 process_video.py ~/Movies/my_video.mp4

# From Desktop
python3 process_video.py ~/Desktop/video.mp4

# Current directory
python3 process_video.py ./my_video.mp4
```

---

## 💡 Pro Tips for Mac

### 1. Create an Alias (Optional)

Add to your `~/.zshrc` file:
```bash
alias process-video="cd ~/path/to/AI-model && python3 process_video.py"
```

Then use:
```bash
process-video ~/Downloads/video.mp4
```

### 2. Drag & Drop in Terminal

You can drag a video file from Finder into Terminal instead of typing the path!

```bash
python3 process_video.py [drag video file here]
```

### 3. Process Multiple Videos

```bash
for video in ~/Downloads/*.mp4; do
    python3 process_video.py "$video"
done
```

### 4. Check What's Running

If it seems stuck, it's probably downloading the Whisper model (first time only):
```bash
# Open Activity Monitor
# Look for "Python" - you'll see it using CPU/GPU
```

---

## 🔧 System Requirements (Mac)

| Component | Requirement | Your Mac |
|-----------|-------------|----------|
| **macOS** | 10.15+ (Catalina or newer) | Check: `sw_vers` |
| **Python** | 3.9+ | Check: `python3 --version` |
| **RAM** | 4GB minimum, 8GB recommended | Check: Apple Menu → About This Mac |
| **Storage** | 2GB free space | For models & dependencies |
| **Internet** | Required | For Google Gemini API |

---

## 🚀 First Run (What to Expect)

When you run the script for the **first time**:

1. **Downloading Whisper model** (~150MB)
   - Takes 1-2 minutes
   - Shows progress bar
   - Only happens once!

2. **GPU Detection**
   ```
   ✅ CUDA GPU detected: [Not on Mac]
   🚀 Using GPU acceleration (Apple Metal)  ← You'll see this on M1/M2/M3
   💻 Using CPU: [processor name]  ← Or this on Intel Mac
   ```

3. **Processing Time**
   - First run: 3-5 minutes (includes downloads)
   - Later runs: 2-3 minutes
   - M1/M2/M3 Macs: Even faster! (~1-2 minutes)

---

## 📊 What Gets Created

```
AI-model/
├── outputs/
│   ├── test_video_1_analysis.docx  ← Word doc (summary, insights, quiz)
│   └── test_video_1_subtitles.srt  ← Subtitle file
│
└── temp_audio/
    └── test_video_1_audio.wav      ← Temporary (auto-deleted)
```

---

## 🆘 Getting Help

If something doesn't work:

1. **Check Python version**
   ```bash
   python3 --version  # Should be 3.9 or higher
   ```

2. **Check if dependencies installed**
   ```bash
   pip3 list | grep whisper
   ```

3. **Check API key**
   ```bash
   cat .env | grep GOOGLE_API_KEY
   ```

4. **Read error message carefully**
   - Most errors tell you exactly what's wrong
   - Google the error message if unclear

5. **Try with virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python process_video.py test_videos/test_video_1.mp4
   ```

---

## ✅ Verification Test

Run this to make sure everything works:

```bash
# Test 1: Python installed
python3 --version

# Test 2: In correct directory
pwd  # Should end with /AI-model

# Test 3: Files exist
ls -la .env requirements.txt process_video.py

# Test 4: Dependencies installed
pip3 list | grep -E "whisper|torch|docx"

# Test 5: Process test video
python3 process_video.py test_videos/test_video_1.mp4

# Test 6: Check output
ls -la outputs/
open outputs/
```

If all 6 tests pass, you're good to go! 🎉

---

## 🎯 Quick Command Reference

```bash
# Setup (once)
pip3 install -r requirements.txt
nano .env  # Add your Google API key

# Process video (every time)
python3 process_video.py your_video.mp4

# Check outputs
open outputs/

# See what's in outputs
ls -la outputs/

# Clean up old outputs (optional)
rm -rf outputs/*
```

---

## 🔄 Updating the Code

If the repository gets updated:

```bash
# Pull latest changes
git pull origin main

# Reinstall dependencies (if requirements changed)
pip3 install -r requirements.txt --upgrade

# Test again
python3 process_video.py test_videos/test_video_1.mp4
```

---

## 🍎 macOS-Specific Features

### Finder Integration

You can open output files directly from Terminal:
```bash
# Open Word document
open outputs/test_video_1_analysis.docx

# Open in Finder
open outputs/

# Open with specific app
open -a "Microsoft Word" outputs/test_video_1_analysis.docx
```

### Notification When Done

Add this to get a notification when processing finishes:
```bash
python3 process_video.py video.mp4 && osascript -e 'display notification "Video processing complete!" with title "AI Video Assistant"'
```

---

**Ready to transform your educational videos on Mac?** 🚀

Just follow steps 1-7 above and you're done in 5 minutes!
