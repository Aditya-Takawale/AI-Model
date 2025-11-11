# 🚀 Setup Guide - Step by Step

This guide will get you up and running in **5 minutes** on any platform.

---

## 📋 Prerequisites

- Python 3.9 or higher installed
- Internet connection (for API and downloading models)

---

## 🔥 Quick Setup (All Platforms)

### Step 1: Clone/Download This Repository

```bash
# If you got this as a zip file
unzip AI-model.zip
cd AI-model

# OR if you're cloning from GitHub
git clone <your-repo-url>
cd AI-model
```

### Step 2: Install Python Dependencies

**One command for all platforms:**

```bash
pip install -r requirements.txt
```

This installs everything you need:
- OpenAI Whisper (for transcription)
- Google AI client
- Video processing libraries
- Document generation tools

### Step 3: Get Your Free Google Gemini API Key

1. Visit: **https://makersuite.google.com/app/apikey**
2. Click "Create API Key"
3. Copy the key (looks like: `AIzaSy...`)

### Step 4: Add Your API Key

Open the `.env` file and add your key:

```bash
GOOGLE_API_KEY=AIzaSyYourActualKeyHere
```

Save and close.

### Step 5: Test It!

```bash
python process_video.py test_videos/test_video_1.mp4
```

You should see:
1. Audio extraction
2. Whisper transcription (GPU will be detected automatically)
3. Google Gemini analysis
4. Output files created

**Done!** 🎉 Check the `outputs/` folder for your results!

---

## 🖥️ Platform-Specific Instructions

### Windows

```powershell
# 1. Open PowerShell or Command Prompt

# 2. Navigate to the folder
cd C:\path\to\AI-model

# 3. Install dependencies
pip install -r requirements.txt

# 4. Edit .env file (use Notepad)
notepad .env
# Add: GOOGLE_API_KEY=your_key_here

# 5. Process a video
python process_video.py test_videos\test_video_1.mp4

# 6. Check outputs
explorer outputs
```

### macOS

```bash
# 1. Open Terminal

# 2. Navigate to the folder
cd ~/Downloads/AI-model

# 3. Install dependencies
pip3 install -r requirements.txt

# 4. Edit .env file
nano .env
# Add: GOOGLE_API_KEY=your_key_here
# Press Ctrl+X, then Y, then Enter to save

# 5. Process a video
python3 process_video.py test_videos/test_video_1.mp4

# 6. Check outputs
open outputs
```

### Linux (Ubuntu/Debian)

```bash
# 1. Open Terminal

# 2. Navigate to the folder
cd ~/AI-model

# 3. Install Python and pip (if not installed)
sudo apt update
sudo apt install python3 python3-pip

# 4. Install dependencies
pip3 install -r requirements.txt

# 5. Edit .env file
nano .env
# Add: GOOGLE_API_KEY=your_key_here
# Press Ctrl+X, then Y, then Enter to save

# 6. Process a video
python3 process_video.py test_videos/test_video_1.mp4

# 7. Check outputs
ls -la outputs/
```

### Server (Headless Linux)

```bash
# 1. Connect via SSH
ssh user@your-server.com

# 2. Upload the AI-model folder (use scp or git clone)
git clone <your-repo-url>
cd AI-model

# 3. Create virtual environment (recommended for servers)
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Edit .env file
nano .env
# Add: GOOGLE_API_KEY=your_key_here

# 6. Process videos
python process_video.py your_video.mp4

# 7. Download results
# Use scp to download outputs folder:
# scp -r user@server:/path/to/AI-model/outputs ./
```

---

## 🔍 Verification Checklist

After setup, verify everything works:

- [ ] Python 3.9+ installed: `python --version` or `python3 --version`
- [ ] Dependencies installed: `pip list | grep whisper`
- [ ] `.env` file has your API key
- [ ] Test video processes successfully
- [ ] Output files created in `outputs/` folder
- [ ] Word document opens correctly

---

## 🎓 First Time Processing

When you run the script for the first time:

1. **Whisper model download** (~150MB for 'base' model)
   - Only happens once
   - Stored in: `~/.cache/whisper/`
   - Takes 1-2 minutes depending on internet speed

2. **GPU detection**
   - Script automatically detects CUDA (NVIDIA) or Metal (Apple Silicon)
   - Falls back to CPU if no GPU found
   - You'll see: "🚀 Using GPU acceleration (CUDA)" or similar

3. **Processing time**
   - First run: 3-5 minutes (includes model download)
   - Subsequent runs: 2-3 minutes

---

## 🔧 Optional: Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

### Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To deactivate later:
```bash
deactivate
```

---

## 🆘 Common Setup Issues

### Issue: "python: command not found"

**Solution:**
- macOS/Linux: Use `python3` instead of `python`
- Windows: Reinstall Python from python.org and check "Add to PATH"

### Issue: "pip: command not found"

**Solution:**
```bash
# macOS/Linux
python3 -m pip install -r requirements.txt

# Windows
python -m pip install -r requirements.txt
```

### Issue: "Permission denied" (Linux/macOS)

**Solution:**
```bash
# Option 1: Install for current user only
pip3 install --user -r requirements.txt

# Option 2: Use sudo (not recommended)
sudo pip3 install -r requirements.txt
```

### Issue: "SSL Certificate Error"

**Solution:**
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Issue: "torch not found" or CUDA errors

**Solution:**
The script works fine without GPU! Just ignore CUDA warnings. But if you want GPU support:

```bash
# For NVIDIA GPU (CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CPU only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

---

## 📱 Mobile/Tablet?

This tool requires Python and is designed for:
- Desktop computers (Windows/Mac/Linux)
- Laptops
- Servers

It won't run natively on phones/tablets, but you can:
- Use a cloud server
- Run on your computer and access via remote desktop
- Use Google Colab (requires modifications)

---

## 🎯 Quick Test Commands

```bash
# Test 1: Check Python version (must be 3.9+)
python --version

# Test 2: Check if dependencies installed
pip list | grep openai-whisper

# Test 3: Verify API key is set
cat .env | grep GOOGLE_API_KEY

# Test 4: Process test video
python process_video.py test_videos/test_video_1.mp4

# Test 5: Check outputs
ls -la outputs/
```

---

## ✅ Setup Complete!

If the test video processed successfully, you're all set!

Now you can:
1. Process your own videos: `python process_video.py your_video.mp4`
2. Check outputs in the `outputs/` folder
3. Share the Word documents with others

---

## 📧 Need Help?

If you're stuck:
1. Check the Troubleshooting section in README.md
2. Make sure your API key is correct in `.env`
3. Try running with `--help` flag: `python process_video.py --help`
4. Open an issue on GitHub with error details

---

**Happy processing!** 🎬
