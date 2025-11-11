# 🎬 AI Video Assistant# 🎬 AI Video Assistant - Production Ready# 🎬 AI Video Lecture Assistant



**Transform educational videos into professional summaries, quizzes, and subtitles using AI**



✅ Works on: **Windows, macOS, Linux, Servers**  **Transform educational videos into transcripts, summaries, quizzes, and subtitled videos using AI****Automatically transcribe, analyze, and add subtitles to educational videos using AI**

⚡ Fast: **2-3 minutes per video**  

💰 Cost: **FREE** (Google Gemini free tier)  

🚀 Simple: **Just ONE command**

✅ **Works on**: Windows, macOS, Linux, Servers  Transform your video lectures into searchable transcripts, insightful summaries, study quizzes, and videos with professional subtitles - all running **100% locally** with no API costs!

---

⚡ **Fast processing**: 2-3 minutes with cloud APIs  

## 🎯 Quick Start (2 Minutes)

💰 **Cost-effective**: ~$0.002 per video (or FREE with Groq)  **Created by [Aditya Takawale](https://github.com/Aditya-Takawale)**

### Step 1: Install Dependencies

🔒 **Flexible**: Local (Ollama) or Cloud (API) modes

```bash

pip install -r requirements.txt---

```

---

### Step 2: Add Your API Key

## ✨ Features

1. Get a **FREE** Google Gemini API key: https://makersuite.google.com/app/apikey

2. Open the `.env` file## 🚀 Quick Start (5 Minutes)

3. Replace the API key:

   ```- 🎤 **Accurate Transcription** - Powered by OpenAI Whisper (supports 99+ languages)

   GOOGLE_API_KEY=your_key_here

   ```### Step 1: Install Python Requirements- 🤖 **AI Analysis** - Generate summaries, key insights, and quiz questions



### Step 3: Process Your Video  - **Local Mode**: Free with Ollama (slower)



```bash```bash  - **Cloud Mode**: Fast with OpenAI/Groq/Anthropic APIs (recommended!)

python process_video.py your_video.mp4

```# Install all dependencies with one command- 📺 **Embedded Subtitles** - Creates video files with toggleable subtitle tracks



**That's it!** 🎉pip install -r requirements.txt- 📄 **Word Documents** - Professional analysis reports in .docx format



---```- 🔒 **Privacy Options** - Run 100% local OR use cloud APIs



## 📦 What You Get- ⚡ **Flexible Performance** - Choose speed vs cost based on your needs



After processing, you'll find in the `outputs/` folder:### Step 2: Get Free API Key (Recommended: Groq)



- **📄 Word Document** - Professional analysis with:---

  - Summary of the video content

  - 7 key insights/takeaways1. Visit **https://console.groq.com**

  - 5-question multiple choice quiz with answers

2. Sign up (free account)## 🚀 Quick Start

- **📝 Subtitle File (.srt)** - Can be used with any video player

3. Create API key (starts with `gsk_`)

---

4. Copy the key### Prerequisites

## 🖥️ Works Everywhere



### Windows

```powershell### Step 3: Configure API Key1. **Python 3.9+** installed

pip install -r requirements.txt

python process_video.py video.mp42. **FFmpeg** installed (see platform-specific instructions below)

```

```bash3. **Ollama** installed and running ([Download here](https://ollama.ai))

### macOS

```bash# Copy example config

pip3 install -r requirements.txt

python3 process_video.py video.mp4cp .env.example .env### Platform-Specific Setup

```



### Linux (Ubuntu/Debian)

```bash# Edit .env and add your key:<details>

pip3 install -r requirements.txt

python3 process_video.py video.mp4# GROQ_API_KEY=gsk_your_key_here<summary><b>🪟 Windows Setup</b></summary>

```

```

### Server / Docker

```bash```powershell

python3 -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate### Step 4: Process Your First Video# 1. Install FFmpeg (choose one method)

pip install -r requirements.txt

python process_video.py video.mp4# Method A: Using Chocolatey (recommended)

```

```bashchoco install ffmpeg

---

python process_with_api.py your_video.mp4

## 🧪 Test It First

```# Method B: Using Scoop

We included a test video. Try it:

scoop install ffmpeg

```bash

python process_video.py test_videos/test_video_1.mp4**That's it!** 🎉

```

# Method C: Manual download from https://ffmpeg.org/download.html

You should see the analysis in about 2-3 minutes!

---

---

# 2. Verify FFmpeg installation

## ⚙️ Configuration

## 📦 What You Getffmpeg -version

The `.env` file contains all settings:



```bash

# Your Google Gemini API key (Required)After processing `lecture.mp4`, you'll find in `outputs/`:# 3. Install Ollama from https://ollama.ai

GOOGLE_API_KEY=your_key_here

# 4. Continue with "Installation" steps below

# Whisper model size (optional)

# Options: tiny, base, small, medium, large- `lecture_with_subtitles.mp4` - Video with embedded subtitles```

# Default: base (recommended)

WHISPER_MODEL=base- `lecture_subtitles.srt` - Standalone subtitle file  </details>

```

- `lecture_analysis.docx` - Word document with summary, insights, quiz

### Whisper Model Comparison:

- `lecture_analysis.json` - Raw JSON data<details>

| Model | Speed | Accuracy | File Size |

|-------|-------|----------|-----------|<summary><b>🍎 macOS Setup</b></summary>

| tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ | 75 MB |

| **base** | ⚡⚡⚡⚡ | ⭐⭐⭐ | 142 MB |---

| small | ⚡⚡⚡ | ⭐⭐⭐⭐ | 466 MB |

| medium | ⚡⚡ | ⭐⭐⭐⭐⭐ | 1.5 GB |```bash

| large | ⚡ | ⭐⭐⭐⭐⭐ | 2.9 GB |

## 💡 API Providers (Choose One)# 1. Install Homebrew (if not installed)

**Recommendation**: Use `base` (default) for best speed/accuracy balance.

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

---

### Option 1: Groq (Recommended - FREE!)

## 🔧 Advanced Usage

# 2. Install FFmpeg

### Process Multiple Videos

```bashbrew install ffmpeg

```bash

python process_video.py video1.mp4# .env file

python process_video.py video2.mp4

python process_video.py video3.mp4GROQ_API_KEY=gsk_your_key_here# 3. Install Ollama

```

```brew install ollama

### Use Different Whisper Model



Edit `.env` and change:

```bash- **Cost**: FREE# 4. Verify installations

WHISPER_MODEL=small  # Better accuracy, slower

```- **Speed**: ⚡ 1-2 secondsffmpeg -version



### Custom Output Directory- **Sign up**: https://console.groq.comollama --version



The script always uses `outputs/` folder. Files are named based on your video name.



---### Option 2: OpenAI# 5. Continue with "Installation" steps below



## 🚨 Troubleshooting```



### "GOOGLE_API_KEY not found"```bash</details>

- Open `.env` file and add your API key

- Get free key: https://makersuite.google.com/app/apikey# .env file



### "Invalid API key" or "API_KEY_INVALID"OPENAI_API_KEY=sk_your_key_here<details>

- Check your key is copied correctly (no extra spaces)

- Generate a new key if needed```<summary><b>🐧 Linux Setup</b></summary>



### "403 Forbidden" or "Quota exceeded"

- You've hit the free tier limit (60 requests/minute)

- Wait a few minutes and try again- **Cost**: ~$0.002 per video```bash

- Google's free tier is very generous!

- **Speed**: ⚡ 2-4 seconds  # Ubuntu/Debian

### "Module not found"

```bash- **Sign up**: https://platform.openai.comsudo apt update

pip install -r requirements.txt --force-reinstall

```sudo apt install ffmpeg



### "FFmpeg not found" (rare)### Option 3: Anthropic Claudecurl -fsSL https://ollama.ai/install.sh | sh

The library uses `imageio-ffmpeg` which installs automatically. But if you see this error:



**Windows:**

```powershell```bash# Fedora/RHEL

choco install ffmpeg

```# .env filesudo dnf install ffmpeg



**macOS:**ANTHROPIC_API_KEY=sk-ant_your_key_herecurl -fsSL https://ollama.ai/install.sh | sh

```bash

brew install ffmpeg```

```

# Arch Linux

**Linux:**

```bash- **Cost**: ~$0.005 per videosudo pacman -S ffmpeg

sudo apt install ffmpeg

```- **Speed**: ⚡ 3-5 secondscurl -fsSL https://ollama.ai/install.sh | sh



---- **Sign up**: https://console.anthropic.com



## 💰 Cost & Limits# Verify installations



### Google Gemini Free Tier:### Option 4: xAI (Grok)ffmpeg -version

- **Cost**: FREE

- **Limit**: 60 requests per minuteollama --version

- **Quality**: Excellent (Gemini 2.5 Flash)

```bash

For a 10-minute video:

- **Cost**: $0.00 (free!)# .env file# Continue with "Installation" steps below

- **Time**: 2-3 minutes

- **Requests**: 1 API callXAI_API_KEY=xai_your_key_here```



You can process **hundreds of videos per day** for free!```</details>



---



## 🎓 What It Does- **Cost**: Pay as you go### Installation



1. **Extracts audio** from your video- **Speed**: ⚡ 2-3 seconds

2. **Transcribes speech** using OpenAI Whisper (runs locally)

3. **Analyzes content** using Google Gemini AI- **Sign up**: https://console.x.ai  **Windows:**

4. **Generates**:

   - Concise summary- **Note**: Requires credits purchase```powershell

   - Key insights/takeaways

   - Multiple-choice quiz with answers# 1. Clone/download this repository

   - Subtitle file (.srt)

5. **Creates Word document** with all analysis---cd c:\Developer\ai-summary



---



## 📖 Documentation## 🔧 Advanced Usage# 2. Create virtual environment



- **[API Usage Guide](docs/API_USAGE_GUIDE.md)** - Advanced API optionspython -m venv .venv

- **[Cross-Platform Guide](docs/CROSS_PLATFORM_GUIDE.md)** - Platform-specific setup

- **[Example Script](examples/use_api.py)** - Python API usage### Basic Usage



---# 3. Activate virtual environment



## 🤝 System Requirements```bash.venv\Scripts\activate



- **Python**: 3.9 or higher# Process with default settings (Groq)

- **RAM**: 2GB minimum (4GB recommended)

- **Disk Space**: 500MB for modelspython process_with_api.py video.mp4# 4. Install dependencies

- **Internet**: Required for Google Gemini API

- **GPU**: Optional (speeds up Whisper, but not required)```pip install -r requirements.txt



### GPU Support:

- **NVIDIA GPU**: Automatically detected and used (CUDA)

- **Apple Silicon (M1/M2/M3)**: Automatically detected and used (Metal)### Choose Different Provider# 5. Start Ollama (in a separate terminal)

- **No GPU**: Works fine on CPU (slightly slower)

ollama serve

---

```bash

## 📝 Example Output

# Use OpenAI# 6. Pull the AI model

After processing a video about Python programming:

python process_with_api.py video.mp4 --provider openaiollama pull llama3.1

```

📊 SUMMARY:```

This lecture introduces Python programming language, covering its history,

key features, and basic syntax. The instructor demonstrates how Python's# Use Anthropic Claude

simple and readable syntax makes it ideal for beginners...

python process_with_api.py video.mp4 --provider anthropic**macOS/Linux:**

💡 KEY INSIGHTS:

1. Python was created by Guido van Rossum and released in 1991```bash

2. Python uses indentation for code blocks instead of braces

3. The language supports multiple programming paradigms...# Use xAI Grok# 1. Clone/download this repository



📝 QUIZ:python process_with_api.py video.mp4 --provider xaicd ~/ai-summary

Q1: Who created the Python programming language?

  [ ] A. Dennis Ritchie```

  [✓] B. Guido van Rossum

  [ ] C. James Gosling# 2. Create virtual environment

  [ ] D. Bjarne Stroustrup

```### Specify Modelpython3 -m venv .venv



---



## 🔒 Privacy & Security```bash# 3. Activate virtual environment



- Transcription (Whisper) runs **100% locally** on your machine# Use GPT-4 for better qualitysource .venv/bin/activate

- Only the transcription text is sent to Google Gemini API

- Video/audio files never leave your computerpython process_with_api.py video.mp4 --provider openai --model gpt-4

- Your API key is stored in `.env` file (never commit to git)

# 4. Install dependencies

---

# Use different Whisper model for transcriptionpip install -r requirements.txt

## 📜 License

python process_with_api.py video.mp4 --whisper-model small

MIT License - Free for personal and commercial use

```# 5. Start Ollama (in a separate terminal)

---

ollama serve

## 🆘 Support

### Custom Output Directory

- **Issues**: Open an issue on GitHub

- **Email**: Contact the maintainer# 6. Pull the AI model

- **Google Gemini Help**: https://ai.google.dev/

```bashollama pull llama3.1

---

python process_with_api.py video.mp4 --output-dir my_results```

## 🎯 Quick Reference Card

```

```bash

# Setup (once)### ⚡ Easy Usage - Simple Script

pip install -r requirements.txt

# Add your API key to .env file---



# Process video (every time)**Simplest method - Just drag and drop:**

python process_video.py your_video.mp4

## 🐍 Python API Usage```powershell

# Output location

outputs/your_video_analysis.docxprocess_video.bat "my_lecture.mp4"

outputs/your_video_subtitles.srt

``````python```



---import os



## ✨ Features Summaryfrom ai_video_assistant import VideoAssistantOr **drag-and-drop** your video file onto `process_video.bat`!



✅ One command to process any video  

✅ Works on Windows, Mac, Linux, Servers  

✅ FREE with Google Gemini  # Initialize with Groq (FREE!)### Advanced Usage

✅ Automatic GPU detection (CUDA/Metal)  

✅ Professional Word document output  assistant = VideoAssistant(

✅ Subtitle file generation  

✅ No complicated setup      whisper_model="base",```powershell

✅ Fast processing (2-3 minutes)  

✅ High-quality AI analysis      use_api=True,# Full processing with all options



---    api_key=os.getenv("GROQ_API_KEY"),python embed_subtitles.py video.mp4 --keep-srt



**Ready to transform your educational videos? Get started in 2 minutes!** 🚀    api_provider="groq"


)# Use better Whisper model for higher accuracy

python embed_subtitles.py video.mp4 -m small

# Process video

result = assistant.process_video("lecture.mp4")# Custom output directory

python embed_subtitles.py video.mp4 -o my_outputs

# Access results

print(result['summary'])# Use different AI model

print(result['insights'])python embed_subtitles.py video.mp4 --ollama-model llama3.2

print(result['quiz'])```

```

### ⚡ Fast Cloud API Mode (NEW!)

See `examples/use_api.py` for complete examples.

**Too slow with local Ollama?** Use cloud APIs for **5-10x faster** processing!

---

```python

## 🖥️ Platform-Specific Setupfrom ai_video_assistant import VideoAssistant



### Windows# Use Groq (FREE + FASTEST!)

assistant = VideoAssistant(

```powershell    use_api=True,

# Install Python 3.9+ from python.org    api_key="gsk_...",  # Get from https://console.groq.com

# Install dependencies    api_provider="groq"

pip install -r requirements.txt)

result = assistant.process_video("video.mp4")

# Set API key```

$env:GROQ_API_KEY="gsk_..."

**Speed & Cost:**

# Run- **Groq**: FREE, 1-2 seconds (recommended!)

python process_with_api.py video.mp4- **OpenAI**: ~$0.002/video, 2-4 seconds

```- **Local Ollama**: FREE, 10-15 minutes



### macOS📖 **[Complete API Guide](docs/API_USAGE_GUIDE.md)** - OpenAI, Groq, Anthropic support



```bash---

# Install Python

brew install python## 📁 Output Files



# Install dependenciesAfter processing `my_lecture.mp4`, you'll get:

pip3 install -r requirements.txt

```

# Set API key (add to ~/.zshrc)outputs/

export GROQ_API_KEY="gsk_..."├── my_lecture_with_subtitles.mp4  ← Video with embedded subtitle track

├── my_lecture_subtitles.srt       ← Standalone subtitle file

# Run├── my_lecture_analysis.docx       ← Word document with analysis

python3 process_with_api.py video.mp4└── my_lecture_analysis.json       ← JSON data

``````



### Linux (Ubuntu/Debian)### How to Use the Video with Subtitles



```bash1. Open `my_lecture_with_subtitles.mp4` in **VLC**, **Windows Media Player**, or any video player

# Install Python2. Look for the **"Subtitles"** or **"CC"** button in player controls

sudo apt update3. Toggle subtitles **ON/OFF** as needed!

sudo apt install python3 python3-pip

---

# Install dependencies

pip3 install -r requirements.txt## 📦 Distribution Options



# Set API key (add to ~/.bashrc)### Option 1: Share Source Code (Recommended for Developers)

export GROQ_API_KEY="gsk_..."

```powershell

# Run# 1. Share the entire folder

python3 process_with_api.py video.mp4# 2. Recipients install Python + Ollama

```# 3. Recipients run: pip install -r requirements.txt

# 4. Ready to use!

### Server/Docker```



```bash### Option 2: Standalone Executable (For End Users)

# Install in virtual environment

python3 -m venv venv```powershell

source venv/bin/activate  # On Windows: venv\Scripts\activate# Install PyInstaller

pip install -r requirements.txtpip install pyinstaller



# Set API key# Create executable

export GROQ_API_KEY="gsk_..."pyinstaller --onefile --name="AI-Video-Processor" embed_subtitles.py



# Run# Distribute: dist/AI-Video-Processor.exe + include instructions to install Ollama

python process_with_api.py video.mp4```

```

**Note:** Users will still need Ollama installed (AI models are too large to bundle ~4GB+).

---

### Option 3: Complete Installer Package

## ⚙️ Environment Variables

Use **Inno Setup** or **NSIS** to create a professional installer:

Create a `.env` file with your configuration:- Bundles Python runtime

- Auto-installs dependencies

```bash- Creates desktop shortcuts

# Required: Choose ONE API provider- Includes Ollama installer link

GROQ_API_KEY=gsk_your_key_here

# OPENAI_API_KEY=sk_your_key_here---

# ANTHROPIC_API_KEY=sk-ant_your_key_here

# XAI_API_KEY=xai_your_key_here## ⚡ Optimizations & Improvements



# Optional: Default provider (default: groq)### Current Performance

API_PROVIDER=groq- **Processing Time**: ~5-10 minutes for 10-minute video (base model)

- **Accuracy**: 95-99% transcription, 75-90% AI analysis quality

# Optional: Whisper model size (default: base)

# Options: tiny, base, small, medium, large### Suggested Optimizations

WHISPER_MODEL=base

```**1. GPU Acceleration** (Faster transcription)

```python

---# Edit transcriber.py, change:

result = model.transcribe(audio_path, fp16=False)  # CPU

## 📖 Documentation# To:

result = model.transcribe(audio_path, fp16=True)   # GPU (10x faster!)

- **[API Usage Guide](docs/API_USAGE_GUIDE.md)** - Complete API setup and pricing```

- **[Cross-Platform Guide](docs/CROSS_PLATFORM_GUIDE.md)** - Platform-specific instructions

**2. Batch Processing Script**

---```powershell

# Process multiple videos at once

## 🔍 Troubleshootingpython batch_process_all.py videos/*.mp4

```

### "API key not found"

**3. Quality vs Speed Trade-offs**

```bash```powershell

# Make sure .env file exists# Ultra-fast (2-3 min for 10-min video, lower accuracy)

cp .env.example .envpython embed_subtitles.py video.mp4 -m tiny



# Add your key to .env# Balanced (default, 5-10 min)

# GROQ_API_KEY=gsk_your_actual_key_herepython embed_subtitles.py video.mp4 -m base

```

# High quality (15-30 min, best accuracy)

### "403 Forbidden" or "401 Unauthorized"python embed_subtitles.py video.mp4 -m medium

```

- Check your API key is correct

- Verify you have credits (xAI, OpenAI, Anthropic)**4. Model Caching** (Already implemented)

- Free tier limits may apply (Groq: 30 requests/minute)- Whisper model loads once and stays in memory

- Ollama runs as persistent service

### "429 Rate Limit"

**5. Parallel Processing**

- Wait 60 seconds and try again- Process video + audio analysis simultaneously

- Upgrade your API plan- Use multiprocessing for batch operations

- Use a different provider

---

### "Module not found"

## 🔧 Advanced Features to Add

```bash

# Reinstall dependencies**Low-hanging fruit:**

pip install -r requirements.txt --force-reinstall1. ✅ Batch processing multiple videos

```2. ✅ Progress bars with estimated time remaining

3. ✅ Email/notification when long processing completes

### GPU/CUDA issues4. ✅ Custom AI prompts for specialized content



The library will automatically use:**Medium complexity:**

- **CUDA** if NVIDIA GPU detected5. 📹 Chapter detection and timestamps

- **Metal** if Apple Silicon (M1/M2/M3)6. 🎨 Custom subtitle styling (fonts, colors, positioning)

- **CPU** otherwise7. 🌐 Web interface (Flask/FastAPI + React)

8. 📱 Mobile app companion

No GPU required! Works on any machine.

**Advanced:**

---9. 🗣️ Speaker diarization (identify different speakers)

10. 📊 Auto-generate highlight reels

## 💰 Cost Calculator11. 🃏 Anki flashcard export

12. 🔴 Real-time processing during live streams

**Processing 100 videos (10 minutes each):**

---

| Provider | Cost | Speed per video |

|----------|------|-----------------|## 🛠️ Technical Architecture

| Groq | **FREE** | ⚡ 1-2 sec |

| OpenAI GPT-3.5 | $0.20 | ⚡ 2-4 sec |```

| OpenAI GPT-4 | $2.00 | ⚡ 3-5 sec |Video File (.mp4, .avi, etc.)

| Anthropic | $0.50 | ⚡ 3-5 sec |    ↓

| xAI Grok | ~$0.50 | ⚡ 2-3 sec |1. Audio Extraction (moviepy)

    ↓

**Recommendation**: Start with **Groq** (free), upgrade to **GPT-4** if you need better quality.2. Speech-to-Text (Whisper AI) → Timestamped segments

    ↓

---3. Content Analysis (Ollama LLM) → Summary + Insights + Quiz

    ↓

## 🛡️ Security Best Practices4. Subtitle Generation (SRT format)

    ↓

✅ **DO:**5. Subtitle Embedding (FFmpeg) → mov_text codec

- Use environment variables (`.env` file)    ↓

- Add `.env` to `.gitignore` (already done)Output: Video with subtitles + Word doc + JSON

- Rotate API keys regularly```

- Set spending limits in provider dashboard

### Models & Technologies

❌ **DON'T:**- **Whisper** (base model ~140MB) - 99 language support

- Commit API keys to git- **Ollama llama3.1** (~4.7GB) - Local LLM, no API calls

- Share keys in screenshots- **FFmpeg** - Video processing

- Use same key across projects- **python-docx** - Document generation



------



## 📜 License## 📋 System Requirements



MIT License - Free for commercial and personal use**Minimum:**

- OS: Windows 10/11, macOS 10.15+, Linux (Ubuntu 18.04+, Fedora 30+, Arch)

---- RAM: 4GB

- Storage: 8GB (models + videos)

## 🆘 Support- CPU: Any modern processor



- **Issues**: Open an issue on GitHub**Recommended:**

- **API Help**: - RAM: 8GB+

  - Groq: https://console.groq.com/docs- Storage: 20GB+ SSD

  - OpenAI: https://platform.openai.com/docs- GPU: NVIDIA with CUDA support (10x faster on Windows/Linux)

  - Anthropic: https://docs.anthropic.com- GPU: Apple Silicon M1/M2/M3 (Metal acceleration on macOS)

  - xAI: https://docs.x.ai

---

---

## 🐛 Troubleshooting

## 🎯 Quick Reference

### FFmpeg Not Found

```bash

# Install**Error:** `[Errno 2] No such file or directory: 'ffmpeg'`

pip install -r requirements.txt

**Solution:**

# Configure```bash

cp .env.example .env# macOS

# Edit .env and add: GROQ_API_KEY=gsk_...brew install ffmpeg



# Run# Ubuntu/Debian

python process_with_api.py video.mp4sudo apt install ffmpeg



# Get help# Windows (Chocolatey)

python process_with_api.py --helpchoco install ffmpeg

```

# Verify installation

**Need free API key?** → https://console.groq.com (2 minutes signup)ffmpeg -version

```

---

### SSL Certificate Error (macOS)

**Ready to process videos at scale? Let's go!** 🚀

**Error:** `ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]`

**Solution:**
```bash
# Run the Install Certificates command
/Applications/Python\ 3.12/Install\ Certificates.command

# OR use Homebrew Python (includes certificates)
brew install python@3.12
```

### Ollama Connection Error

**Error:** `Connection refused to localhost:11434`

**Solution:**
```bash
# Start Ollama server
ollama serve

# In another terminal, verify model is installed
ollama list
ollama pull llama3.1
```

### Out of Memory Error

**Error:** `RuntimeError: CUDA out of memory`

**Solution:**
```python
# Use a smaller Whisper model
python embed_subtitles.py video.mp4 -m tiny  # or -m base

# Process shorter videos
# Consider splitting long videos into segments
```

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'ai_video_assistant'`

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Reinstall package
pip install -r requirements.txt
```

### Permission Errors (Linux/macOS)

**Error:** `PermissionError: [Errno 13]`

**Solution:**
```bash
# Make sure you have write permissions
chmod +w ./outputs
chmod +w ./temp_audio

# Don't run with sudo unless necessary
```

---

## 👨‍💻 Author

**Aditya Takawale**
- GitHub: [@Aditya-Takawale](https://github.com/Aditya-Takawale)
- Repository: [AI-Summary](https://github.com/Aditya-Takawale/AI-Summary)

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

Copyright © 2025 Aditya Takawale

## 🙏 Acknowledgments

Built with:
- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition (MIT License)
- [Ollama](https://ollama.ai) - Local AI models (MIT License)
- [MoviePy](https://zulko.github.io/moviepy/) - Video processing (MIT License)
- [FFmpeg](https://ffmpeg.org/) - Media processing (LGPL)

This project is an independent integration of these tools and is not affiliated with or endorsed by OpenAI, Ollama, or any of the above projects.

## ⚖️ Disclaimer

This software is provided "as is" for educational and personal use. Users are responsible for:
- Complying with copyright laws when processing videos
- Respecting terms of service of video platforms
- Using this tool ethically and legally
- Not redistributing copyrighted content without permission

The author is not responsible for misuse of this software.

## 🌟 Support

If you find this project helpful, please give it a ⭐️ on GitHub!

**Report Issues:** [GitHub Issues](https://github.com/Aditya-Takawale/AI-Summary/issues)

---

**Built with ❤️ by Aditya Takawale | 100% Local, 100% Free, 100% Private**

---