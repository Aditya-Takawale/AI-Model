# 🧪 Testing Guide

This guide will help you verify everything works correctly before pushing to production.

---

## 🎯 Quick Test (2 minutes)

**Test the simplest video first:**

```bash
python process_video.py test_videos/test_video_1.mp4
```

**Expected result:**
- ✅ Processing completes in 2-3 minutes
- ✅ No errors displayed
- ✅ Files created in `outputs/` folder:
  - `test_video_1_analysis.docx`
  - `test_video_1_subtitles.srt`
- ✅ Word document opens and shows summary, insights, quiz

If this works, **you're good to go!** 🎉

---

## 📹 Test Videos Available

We included 6 test videos covering different topics and lengths:

| Video | Topic | Length | Size | Best For |
|-------|-------|--------|------|----------|
| test_video_1.mp4 | JavaScript Intro | ~7 min | 11 MB | ⭐ **Start here** |
| test_video_2.mp4 | Programming Concepts | ~9 min | 15 MB | General testing |
| test_video_3.mp4 | Tech Tutorial | ~5 min | 7 MB | Quick test |
| test_video_4.mp4 | Cybersecurity | ~14 min | 23 MB | Longer content |
| test_video_5.mp4 | Educational | ~15 min | 25 MB | Extended test |
| test_video_6.mp4 | Lecture | ~20 min | 36 MB | Stress test |

---

## 🔍 Complete Test Checklist

### ✅ Test 1: Basic Setup Verification

```bash
# Check Python version (must be 3.9+)
python --version

# Check if dependencies installed
pip list | grep whisper

# Verify .env file exists and has API key
cat .env
```

**Expected:**
- Python 3.9 or higher
- `openai-whisper` appears in package list
- `.env` file shows your API key

---

### ✅ Test 2: Process Shortest Video (Quick)

```bash
python process_video.py test_videos/test_video_3.mp4
```

**Expected output:**
```
======================================================================
🎬 AI Video Assistant
======================================================================

📹 Video: test_videos/test_video_3.mp4
🤖 AI: Google Gemini 2.5 Flash
🎤 Transcription: Whisper (base)
📂 Output: outputs/

⏳ Processing... This will take 2-3 minutes
======================================================================

[Whisper transcription logs...]
[Google Gemini API call...]

======================================================================
✅ SUCCESS! Video processed successfully!
======================================================================

📊 SUMMARY:
----------------------------------------------------------------------
[Summary text appears here...]

💡 KEY INSIGHTS:
----------------------------------------------------------------------
1. [Insight 1...]
2. [Insight 2...]
...

📝 QUIZ:
----------------------------------------------------------------------
Q1: [Question text...]
  [✓] A. [Correct answer]
  [ ] B. [Wrong answer]
...

======================================================================
📂 OUTPUT FILES:
======================================================================
📄 Analysis: outputs/test_video_3_analysis.docx
📝 Subtitles: outputs/test_video_3_subtitles.srt
======================================================================
```

**Time:** 1-2 minutes (shorter video)

---

### ✅ Test 3: Verify Output Files

```bash
# List output files
ls -la outputs/

# Open Word document (Windows)
start outputs/test_video_3_analysis.docx

# Open Word document (Mac)
open outputs/test_video_3_analysis.docx

# Open Word document (Linux)
libreoffice outputs/test_video_3_analysis.docx
```

**Check in Word document:**
- ✅ Title and video name
- ✅ Summary paragraph (4-6 sentences)
- ✅ 7 key insights (numbered list)
- ✅ 5 quiz questions with 4 options each
- ✅ Correct answers marked with checkboxes
- ✅ Professional formatting

**Check subtitle file:**
```bash
# View first 20 lines of .srt file
head -20 outputs/test_video_3_subtitles.srt
```

**Expected format:**
```
1
00:00:00,000 --> 00:00:02,500
Welcome to this tutorial...

2
00:00:02,500 --> 00:00:05,000
Today we're going to learn...
```

---

### ✅ Test 4: GPU Detection Test

```bash
python process_video.py test_videos/test_video_1.mp4
```

**Look for these messages:**

**With NVIDIA GPU:**
```
INFO:root:✅ CUDA GPU detected: NVIDIA GeForce RTX 3050
INFO:ai_video_assistant.transcriber:🚀 Using GPU acceleration (CUDA)
```

**With Apple Silicon:**
```
INFO:ai_video_assistant.transcriber:🚀 Using GPU acceleration (Apple Metal)
```

**CPU Only:**
```
INFO:ai_video_assistant.transcriber:💻 Using CPU: [processor name]
```

**All are correct!** GPU is optional - CPU works fine.

---

### ✅ Test 5: Different Video Test

Test with a different video to ensure it's not a fluke:

```bash
python process_video.py test_videos/test_video_4.mp4
```

**Expected:**
- ✅ Different content in summary (about cybersecurity)
- ✅ Different insights
- ✅ New quiz questions
- ✅ Files: `test_video_4_analysis.docx` and `test_video_4_subtitles.srt`

---

### ✅ Test 6: Error Handling Test

Test what happens with a bad file:

```bash
python process_video.py nonexistent.mp4
```

**Expected:**
```
❌ Error: Video file not found: nonexistent.mp4
```

Good! Error handling works.

---

### ✅ Test 7: API Key Test

Temporarily break the API key to test error handling:

1. Edit `.env` and change API key to `TEST123`
2. Run: `python process_video.py test_videos/test_video_1.mp4`
3. **Expected:** Clear error message about invalid API key
4. Fix: Restore correct API key in `.env`

---

## 🌍 Platform-Specific Tests

### Windows Test:

```powershell
# Test 1: From current directory
python process_video.py test_videos\test_video_1.mp4

# Test 2: With full path
python process_video.py C:\Developer\AI-model\test_videos\test_video_1.mp4

# Test 3: Open outputs folder
explorer outputs

# Test 4: Open Word doc
start outputs\test_video_1_analysis.docx
```

### macOS Test:

```bash
# Test 1: From current directory
python3 process_video.py test_videos/test_video_1.mp4

# Test 2: With full path
python3 process_video.py ~/AI-model/test_videos/test_video_1.mp4

# Test 3: Open outputs folder
open outputs

# Test 4: Open Word doc
open outputs/test_video_1_analysis.docx
```

### Linux Test:

```bash
# Test 1: From current directory
python3 process_video.py test_videos/test_video_1.mp4

# Test 2: Check outputs
ls -lh outputs/

# Test 3: View Word doc (LibreOffice)
libreoffice outputs/test_video_1_analysis.docx

# Test 4: View subtitle file
cat outputs/test_video_1_subtitles.srt
```

---

## 🚀 Performance Tests

### Test Processing Times:

Process all test videos and measure times:

```bash
# Short video (~5 min)
time python process_video.py test_videos/test_video_3.mp4

# Medium video (~10 min)
time python process_video.py test_videos/test_video_1.mp4

# Long video (~20 min)
time python process_video.py test_videos/test_video_6.mp4
```

**Expected times:**
- Short (5 min video): 1-2 minutes
- Medium (10 min video): 2-3 minutes
- Long (20 min video): 3-5 minutes

**Note:** First run takes longer (downloads Whisper model ~150MB)

---

## 📊 Batch Test

Process multiple videos in sequence:

```bash
python process_video.py test_videos/test_video_1.mp4
python process_video.py test_videos/test_video_2.mp4
python process_video.py test_videos/test_video_3.mp4
```

**Check:** All outputs created correctly in `outputs/` folder

---

## 🔍 Quality Tests

### Test 1: Summary Quality

Open any generated Word document and verify:

- ✅ Summary is coherent and makes sense
- ✅ Summary accurately reflects video content
- ✅ Length is appropriate (4-6 sentences)

### Test 2: Insights Quality

Check that insights:

- ✅ Are distinct (not repetitive)
- ✅ Capture important points
- ✅ Are factually correct from video

### Test 3: Quiz Quality

Verify quiz questions:

- ✅ Questions are clear and specific
- ✅ All 4 options are plausible
- ✅ Correct answer is marked
- ✅ Questions test understanding, not memorization

### Test 4: Subtitle Accuracy

Compare subtitle file to video:

```bash
# View subtitles
cat outputs/test_video_1_subtitles.srt
```

- ✅ Timestamps are correct
- ✅ Text matches spoken words (roughly)
- ✅ Line breaks are reasonable

---

## 🆘 Troubleshooting Tests

### If Processing Fails:

**Check 1: Dependencies**
```bash
pip list | grep -E "whisper|torch|moviepy|requests|docx"
```

All should be installed.

**Check 2: API Key**
```bash
cat .env | grep GOOGLE_API_KEY
```

Should show your valid key.

**Check 3: Internet Connection**
```bash
ping google.com
```

**Check 4: Disk Space**
```bash
df -h .
```

Need at least 1GB free.

**Check 5: Video File**
```bash
file test_videos/test_video_1.mp4
```

Should show it's a valid video file.

---

## ✅ Final Verification Checklist

Before considering testing complete:

- [ ] Processed at least 2 different test videos successfully
- [ ] Output Word documents open and look professional
- [ ] Subtitle files are properly formatted
- [ ] GPU/CPU detection works correctly
- [ ] Error handling works (tested with bad filename)
- [ ] Processing times are reasonable (2-5 min per video)
- [ ] API quota not exceeded (Google allows 60 req/min)
- [ ] Files are created in correct location (`outputs/`)
- [ ] Multiple videos can be processed in sequence
- [ ] Cross-platform path handling works (if testing on multiple OS)

---

## 🎯 Recommended Test Sequence

**For your friend (Mac user):**

```bash
# Step 1: Quick setup verification
python3 --version
pip3 list | grep whisper
cat .env

# Step 2: Process shortest video first
python3 process_video.py test_videos/test_video_3.mp4

# Step 3: Verify output
open outputs/
open outputs/test_video_3_analysis.docx

# Step 4: If that worked, try a different one
python3 process_video.py test_videos/test_video_1.mp4

# Step 5: Verify it works with their own video
python3 process_video.py ~/Desktop/my_video.mp4

# Done! ✅
```

**Expected total time:** 10-15 minutes for complete testing

---

## 📝 Test Report Template

After testing, your friend can confirm:

```
✅ Testing Complete!

Platform: [Windows/Mac/Linux]
Python Version: [3.x.x]
GPU Detected: [Yes (CUDA/Metal) / No (CPU)]

Videos Tested:
- test_video_1.mp4: ✅ Success
- test_video_3.mp4: ✅ Success
- my_own_video.mp4: ✅ Success

Output Quality:
- Summaries: ✅ Accurate and coherent
- Insights: ✅ Relevant and useful
- Quiz: ✅ Clear questions, correct answers
- Subtitles: ✅ Properly formatted

Processing Time:
- Average: 2-3 minutes per 10-min video

Issues Found: None / [List any issues]

Status: ✅ Ready for production!
```

---

## 🎉 Success Criteria

Testing is successful if:

1. ✅ At least 2 test videos process without errors
2. ✅ Output files are created correctly
3. ✅ Word documents open and look professional
4. ✅ Processing completes in reasonable time (2-5 min)
5. ✅ Can process user's own videos

**If all criteria met → Ready to use!** 🚀

---

## 💡 Tips

- **Start with test_video_3.mp4** (shortest, fastest)
- **Don't test all 6 videos at once** (uses API quota)
- **Check outputs/ folder after each test**
- **Open Word docs to verify quality**
- **Test with your own video as final check**

---

**Happy Testing!** 🧪✨
