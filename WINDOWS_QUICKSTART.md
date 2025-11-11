# 🪟 Quick Start Guide for Windows Users

**For anyone who just cloned this repo on Windows**

---

## ⚡ Super Fast Setup (5 Minutes)

### Step 1: Open PowerShell or Command Prompt
Press `Win + R`, type `powershell`, press Enter

### Step 2: Navigate to the Project
```powershell
cd C:\Users\YourName\Downloads\AI-model  # or wherever you cloned it
```

### Step 3: Install Python Dependencies
```powershell
pip install -r requirements.txt
```

**Wait 2-3 minutes** - This downloads all necessary libraries.

### Step 4: Get Your FREE Google Gemini API Key

1. Open this link: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (looks like: `AIzaSy...`)

### Step 5: Add Your API Key

```powershell
# Open the .env file with Notepad
notepad .env

# You'll see:
# GOOGLE_API_KEY=AIzaSyDPMNX0GFFySpAScHYGPhnn1R4V_mvCSfw
#
# Replace the key with YOUR key
# Press Ctrl+S to save, then close Notepad
```

### Step 6: Test It!

```powershell
python process_video.py test_videos\test_video_1.mp4
```

**Expected result:**
- Should take 2-3 minutes
- You'll see processing messages
- Files will be created in `outputs\` folder

### Step 7: Check Your Results

```powershell
explorer outputs
```

You should see:
- ✅ `test_video_1_analysis.docx` - Word document with summary & quiz
- ✅ `test_video_1_subtitles.srt` - Subtitle file

---

## 🎯 That's It!

Now you can process any video:

```powershell
python process_video.py your_video.mp4
```

---

## 🔍 Common Windows Issues & Solutions

### Issue: "python: command not found" or "'python' is not recognized"

**Solution:**
1. Download Python from: https://www.python.org/downloads/
2. **Important**: Check "Add Python to PATH" during installation
3. Restart PowerShell
4. Try again: `python --version`

### Issue: "pip: command not found"

**Solution:**
```powershell
# Use python -m pip instead
python -m pip install -r requirements.txt
```

### Issue: "Permission Denied" or "Access Denied"

**Solution 1 - Run as Administrator:**
```powershell
# Right-click PowerShell → "Run as Administrator"
```

**Solution 2 - Install for user only:**
```powershell
pip install --user -r requirements.txt
```

### Issue: "SSL Certificate Error"

**Solution:**
```powershell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Issue: Long path names causing errors

**Solution:**
```powershell
# Move the folder closer to C:\
# Example: C:\AI-model instead of C:\Users\...\Downloads\AI-model
```

---

## 🎮 Windows with NVIDIA GPU

If you have an NVIDIA graphics card:

**Good news!** The script automatically detects your GPU:
- You'll see: "🚀 Using GPU acceleration (CUDA)"
- Whisper will run **much faster**
- No extra setup needed!

**No GPU?** No problem!
- Script runs fine on CPU
- Just takes a bit longer (~3-5 minutes vs 1-2 minutes)

---

## 🧪 Test Videos Included

We included 6 test videos for you:

```powershell
# Quick test (shortest video - 1 minute)
python process_video.py test_videos\test_video_1.mp4

# Try other videos
python process_video.py test_videos\test_video_2.mp4
python process_video.py test_videos\test_video_3.mp4
python process_video.py test_videos\test_video_4.mp4
python process_video.py test_videos\test_video_5.mp4
python process_video.py test_videos\test_video_6.mp4
```

---

## 📝 Step-by-Step Checklist

- [ ] 1. Open PowerShell
- [ ] 2. Navigate to project: `cd C:\...\AI-model`
- [ ] 3. Install dependencies: `pip install -r requirements.txt`
- [ ] 4. Get Google API key: https://makersuite.google.com/app/apikey
- [ ] 5. Edit .env file: `notepad .env` (add your key)
- [ ] 6. Test: `python process_video.py test_videos\test_video_1.mp4`
- [ ] 7. Check outputs: `explorer outputs`

---

## 🎬 Processing Your Own Videos

```powershell
# From Downloads folder
python process_video.py C:\Users\YourName\Downloads\my_lecture.mp4

# From Videos folder
python process_video.py C:\Users\YourName\Videos\my_video.mp4

# From Desktop
python process_video.py C:\Users\YourName\Desktop\video.mp4

# Current directory
python process_video.py .\my_video.mp4
```

---

## 💡 Pro Tips for Windows

### 1. Create a Batch File (Optional)

Create `process.bat`:
```batch
@echo off
cd C:\path\to\AI-model
python process_video.py %1
pause
```

Then drag & drop videos onto `process.bat`!

### 2. Add to Right-Click Menu

Process videos by right-clicking in Explorer! (Advanced - requires registry edit)

### 3. Process Multiple Videos

```powershell
Get-ChildItem C:\Videos\*.mp4 | ForEach-Object {
    python process_video.py $_.FullName
}
```

### 4. Set Environment Variable Permanently

```powershell
# Set GOOGLE_API_KEY permanently
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'your_key', 'User')
```

---

## 🔧 System Requirements (Windows)

| Component | Requirement | Check |
|-----------|-------------|-------|
| **Windows** | 10 or 11 | Check: Win+Pause |
| **Python** | 3.9+ | `python --version` |
| **RAM** | 4GB minimum, 8GB recommended | Task Manager |
| **Storage** | 2GB free space | C: drive properties |
| **Internet** | Required | For Google Gemini API |
| **GPU** | Optional (NVIDIA) | Check: Device Manager |

---

## 🚀 First Run (What to Expect)

When you run the script for the **first time**:

1. **Downloading Whisper model** (~150MB)
   - Takes 1-2 minutes
   - Shows progress bar
   - Stored in: `C:\Users\YourName\.cache\whisper\`
   - Only happens once!

2. **GPU Detection**
   ```
   ✅ CUDA GPU detected: NVIDIA GeForce RTX 3050
   🚀 Using GPU acceleration (CUDA)  ← If you have NVIDIA GPU
   💻 Using CPU: Intel Core i7  ← Or CPU if no GPU
   ```

3. **Processing Time**
   - First run: 3-5 minutes (includes downloads)
   - With GPU: 1-2 minutes per video
   - With CPU: 2-3 minutes per video

---

## 📊 What Gets Created

```
AI-model\
├── outputs\
│   ├── test_video_1_analysis.docx  ← Word doc (summary, insights, quiz)
│   └── test_video_1_subtitles.srt  ← Subtitle file
│
└── temp_audio\
    └── test_video_1_audio.wav      ← Temporary (auto-deleted)
```

---

## 🆘 Getting Help

If something doesn't work:

1. **Check Python version**
   ```powershell
   python --version  # Should be 3.9 or higher
   ```

2. **Check if dependencies installed**
   ```powershell
   pip list | Select-String whisper
   ```

3. **Check API key**
   ```powershell
   Get-Content .env | Select-String GOOGLE_API_KEY
   ```

4. **Read error message carefully**
   - Most errors tell you exactly what's wrong
   - Google the error message if unclear

5. **Try with virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   python process_video.py test_videos\test_video_1.mp4
   ```

---

## ✅ Verification Test

Run these commands to make sure everything works:

```powershell
# Test 1: Python installed
python --version

# Test 2: In correct directory
pwd  # Should end with \AI-model

# Test 3: Files exist
dir .env, requirements.txt, process_video.py

# Test 4: Dependencies installed
pip list | Select-String -Pattern "whisper|torch|docx"

# Test 5: Process test video
python process_video.py test_videos\test_video_1.mp4

# Test 6: Check output
dir outputs\
explorer outputs
```

If all 6 tests pass, you're good to go! 🎉

---

## 🎯 Quick Command Reference

```powershell
# Setup (once)
pip install -r requirements.txt
notepad .env  # Add your Google API key

# Process video (every time)
python process_video.py your_video.mp4

# Check outputs
explorer outputs

# See what's in outputs
dir outputs

# Clean up old outputs (optional)
Remove-Item outputs\* -Recurse
```

---

## 🔄 Updating the Code

If the repository gets updated:

```powershell
# Pull latest changes
git pull origin main

# Reinstall dependencies (if requirements changed)
pip install -r requirements.txt --upgrade

# Test again
python process_video.py test_videos\test_video_1.mp4
```

---

## 🪟 Windows-Specific Features

### File Explorer Integration

You can open files directly from PowerShell:
```powershell
# Open Word document
Start-Process outputs\test_video_1_analysis.docx

# Open folder in Explorer
explorer outputs

# Open with specific app
Start-Process "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE" outputs\test_video_1_analysis.docx
```

### Windows Notification When Done

```powershell
python process_video.py video.mp4; Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Video processing complete!', 'AI Video Assistant')
```

### Task Scheduler Integration

You can set up automated processing using Windows Task Scheduler!

---

**Ready to transform your educational videos on Windows?** 🚀

Just follow steps 1-7 above and you're done in 5 minutes!
