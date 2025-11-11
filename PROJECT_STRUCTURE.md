# 📁 Project Structure

```
AI-model/
│
├── 📄 process_video.py          # ⭐ MAIN SCRIPT - Your friend runs this!
├── 📄 .env                       # ⚙️  Configuration (API key goes here)
├── 📄 .env.example               # Example configuration
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # Main documentation
├── 📄 SETUP.md                   # Detailed setup instructions
├── 📄 LICENSE                    # MIT License
├── 📄 .gitignore                 # Git ignore rules
│
├── 📁 ai_video_assistant/        # Core library (don't modify)
│   ├── __init__.py
│   ├── core.py                  # Main VideoAssistant class
│   ├── transcriber.py           # Whisper transcription
│   ├── api_analyzer.py          # Google Gemini API integration
│   ├── analyzer.py              # Local Ollama (alternative)
│   ├── audio_extractor.py       # Extract audio from video
│   ├── subtitle_generator.py    # Generate .srt files
│   ├── word_generator.py        # Generate .docx files
│   └── ffmpeg_utils.py          # FFmpeg detection
│
├── 📁 docs/                      # Documentation
│   ├── API_USAGE_GUIDE.md       # Advanced API options
│   └── CROSS_PLATFORM_GUIDE.md  # Platform-specific guides
│
├── 📁 examples/                  # Example scripts
│   └── use_api.py               # Python API usage example
│
├── 📁 test_videos/               # Sample videos for testing
│   └── test_video_1.mp4         # Test this first!
│
├── 📁 outputs/                   # Generated files appear here
│   ├── *.docx                   # Word documents with analysis
│   └── *.srt                    # Subtitle files
│
└── 📁 temp_audio/                # Temporary audio files (auto-created)
    └── *.wav                    # Extracted audio (auto-deleted)
```

---

## 🎯 Key Files for Your Friend

### **Must Edit:**
- **`.env`** - Add Google API key here

### **Must Run:**
- **`process_video.py`** - The main script

### **Should Read:**
- **`README.md`** - Quick start guide
- **`SETUP.md`** - Detailed setup instructions

### **Don't Touch:**
- `ai_video_assistant/` folder - Core library code
- `setup.py` - For package installation

---

## 🚀 Workflow

```
1. Clone repository
   ↓
2. pip install -r requirements.txt
   ↓
3. Edit .env (add API key)
   ↓
4. python process_video.py video.mp4
   ↓
5. Check outputs/ folder
```

---

## 📦 What Gets Created

When you run `python process_video.py my_video.mp4`:

```
outputs/
├── my_video_analysis.docx    # ← Word document (summary, insights, quiz)
└── my_video_subtitles.srt    # ← Subtitle file

temp_audio/
└── my_video_audio.wav         # ← Temporary (auto-deleted after processing)
```

---

## 🔧 Configuration Files

### `.env` (Main config)
```bash
GOOGLE_API_KEY=your_key_here    # Required
WHISPER_MODEL=base              # Optional (default: base)
API_PROVIDER=google             # Optional (default: google)
```

### `requirements.txt` (Dependencies)
- `openai-whisper` - Speech-to-text
- `requests` - API calls
- `python-dotenv` - Environment variables
- `python-docx` - Word document generation
- `moviepy` - Video processing
- `torch` - Machine learning backend
- And more...

---

## 📊 File Sizes

| File/Folder | Size | Purpose |
|-------------|------|---------|
| `requirements.txt` | 1 KB | Dependency list |
| `.env` | 1 KB | Configuration |
| `process_video.py` | 5 KB | Main script |
| `ai_video_assistant/` | 50 KB | Core library |
| `test_videos/` | 5-10 MB | Sample videos |
| **First download** | ~500 MB | Whisper model + PyTorch |

---

## 🔒 Security Notes

### ✅ Safe to commit to Git:
- All code files
- `README.md`, `SETUP.md`
- `.env.example`
- `.gitignore`

### ❌ Never commit to Git:
- `.env` (contains API key)
- `outputs/` folder
- `temp_audio/` folder
- `__pycache__/`

The `.gitignore` file is already configured correctly!

---

## 🌍 Cross-Platform Compatibility

| Feature | Windows | macOS | Linux | Server |
|---------|---------|-------|-------|--------|
| Python script | ✅ | ✅ | ✅ | ✅ |
| GPU (CUDA) | ✅ | ❌ | ✅ | ✅ |
| GPU (Metal) | ❌ | ✅ (M1/M2/M3) | ❌ | ❌ |
| CPU fallback | ✅ | ✅ | ✅ | ✅ |
| File paths | Auto-detected | Auto-detected | Auto-detected | Auto-detected |

Everything works everywhere! The code automatically detects the platform.

---

## 📝 Module Breakdown

### `core.py` - VideoAssistant Class
Main orchestrator that:
- Initializes all components
- Manages the processing pipeline
- Handles API vs local mode

### `transcriber.py` - AudioTranscriber Class
- Loads Whisper model
- Detects GPU (CUDA/Metal/CPU)
- Transcribes audio to text

### `api_analyzer.py` - APIContentAnalyzer Class
- Connects to Google Gemini API
- Sends transcription
- Parses AI response (summary, insights, quiz)

### `audio_extractor.py`
- Extracts audio from video files
- Converts to WAV format
- Handles different video formats

### `word_generator.py`
- Creates professional Word documents
- Formats summary, insights, quiz
- Adds headers and styling

### `subtitle_generator.py`
- Generates .srt subtitle files
- Proper timestamp formatting
- Compatible with all video players

---

## 🔄 Processing Pipeline

```
Video File (MP4, AVI, etc.)
    ↓
[audio_extractor.py]
    ↓
Audio File (WAV)
    ↓
[transcriber.py] - Whisper
    ↓
Transcription (Text)
    ↓
[api_analyzer.py] - Google Gemini
    ↓
Analysis (JSON)
    ↓
[word_generator.py] - Word Doc
[subtitle_generator.py] - SRT File
    ↓
outputs/ folder
```

---

## 💡 Tips for Your Friend

### Quick Commands:
```bash
# Test setup
python process_video.py test_videos/test_video_1.mp4

# Process their own video
python process_video.py ~/Downloads/my_lecture.mp4

# Change Whisper model (edit .env)
WHISPER_MODEL=small  # Better accuracy

# Check what was created
ls -la outputs/
```

### Common Paths:
- Windows: `python process_video.py C:\Users\Name\Videos\video.mp4`
- macOS: `python3 process_video.py ~/Movies/video.mp4`
- Linux: `python3 process_video.py ~/Videos/video.mp4`

---

## ✨ That's It!

The structure is simple:
1. Main script: `process_video.py`
2. Config file: `.env`
3. Output folder: `outputs/`

Everything else is library code that just works! 🚀
