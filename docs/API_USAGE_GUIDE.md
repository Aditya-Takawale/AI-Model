# API Usage Guide

This guide shows how to use **cloud APIs** (OpenAI, Groq, Anthropic) instead of local Ollama for faster processing.

## Why Use Cloud APIs?

**Advantages:**
- ⚡ **MUCH FASTER**: 2-3 minutes vs 10-15 minutes with local Ollama
- 🖥️ **No GPU needed**: Works on any machine
- 🎯 **More reliable**: Professional infrastructure
- 💰 **Very cheap**: ~$0.002 per 10-minute video

**Use Cases:**
- You don't have a powerful GPU
- You're on Mac M1/M2/M3 and Ollama is too slow
- You need faster processing for production
- Running on a server without GPU

---

## Supported Providers

### 1. Groq (Recommended for Speed)

**⚡ FASTEST OPTION** - Processes in 1-2 seconds!

```python
from ai_video_assistant import VideoAssistant

assistant = VideoAssistant(
    use_api=True,
    api_key="gsk_...",  # Get from https://console.groq.com
    api_provider="groq",
    api_model="llama-3.1-8b-instant"  # FREE with rate limits
)
```

- **Cost**: FREE (with generous rate limits)
- **Speed**: 1-2 seconds per analysis
- **Model**: Llama 3.1 8B (very capable)
- **Sign up**: https://console.groq.com

### 2. OpenAI (Most Reliable)

**🏆 BEST QUALITY & RELIABILITY**

```python
assistant = VideoAssistant(
    use_api=True,
    api_key="sk-...",  # Get from https://platform.openai.com/api-keys
    api_provider="openai",
    api_model="gpt-3.5-turbo"  # or "gpt-4" for even better quality
)
```

- **Cost**: ~$0.002 per video (GPT-3.5), ~$0.02 (GPT-4)
- **Speed**: 2-4 seconds per analysis
- **Model**: GPT-3.5 Turbo (very good) or GPT-4 (excellent)
- **Sign up**: https://platform.openai.com

### 3. Anthropic Claude

**🧠 EXCELLENT REASONING**

```python
assistant = VideoAssistant(
    use_api=True,
    api_key="sk-ant-...",  # Get from https://console.anthropic.com
    api_provider="anthropic",
    api_model="claude-3-haiku-20240307"
)
```

- **Cost**: ~$0.005 per video
- **Speed**: 3-5 seconds per analysis
- **Model**: Claude 3 Haiku (fast & smart)
- **Sign up**: https://console.anthropic.com

---

## Complete Example

```python
import os
from ai_video_assistant import VideoAssistant

# Method 1: Use environment variable (RECOMMENDED)
api_key = os.getenv("GROQ_API_KEY")

# Method 2: Hardcode (for testing only)
api_key = "gsk_your_key_here"

# Initialize with API
assistant = VideoAssistant(
    whisper_model="base",      # Whisper still runs locally
    use_api=True,              # Enable API mode
    api_key=api_key,
    api_provider="groq",       # or "openai" or "anthropic"
    api_model="llama-3.1-8b-instant"
)

# Process video (same API as before!)
result = assistant.process_video("lecture.mp4")

print(result['summary'])
print(result['quiz'])
```

---

## Cost Comparison

Processing a **10-minute lecture video**:

| Provider | Model | Cost | Speed |
|----------|-------|------|-------|
| **Groq** | Llama 3.1 8B | FREE | ⚡ 1-2 sec |
| **OpenAI** | GPT-3.5 Turbo | $0.002 | ⚡ 2-4 sec |
| **OpenAI** | GPT-4 | $0.02 | ⚡ 3-5 sec |
| **Anthropic** | Claude 3 Haiku | $0.005 | ⚡ 3-5 sec |
| **Ollama (Local)** | Llama 3.1 8B | FREE | 🐌 10-15 min |

**Recommendation**: Start with **Groq** (free + fastest), upgrade to OpenAI GPT-4 if you need better quality.

---

## Getting API Keys

### Groq (FREE)
1. Visit https://console.groq.com
2. Sign up with email
3. Go to **API Keys** section
4. Create new key (starts with `gsk_`)
5. Free tier: 30 requests/minute

### OpenAI
1. Visit https://platform.openai.com
2. Sign up and add payment method ($5 minimum)
3. Go to **API Keys** → **Create new key**
4. Key starts with `sk-`
5. Check usage: https://platform.openai.com/usage

### Anthropic
1. Visit https://console.anthropic.com
2. Sign up and add payment method
3. Go to **API Keys** → **Create Key**
4. Key starts with `sk-ant-`

---

## Environment Variables (Recommended)

**Why?** Never hardcode API keys in your code!

### Windows (PowerShell)
```powershell
# Set for current session
$env:GROQ_API_KEY="gsk_..."
$env:OPENAI_API_KEY="sk-..."

# Set permanently
[System.Environment]::SetEnvironmentVariable('GROQ_API_KEY','gsk_...','User')
```

### macOS/Linux (Bash)
```bash
# Add to ~/.bashrc or ~/.zshrc
export GROQ_API_KEY="gsk_..."
export OPENAI_API_KEY="sk_..."

# Reload
source ~/.bashrc
```

### In Python
```python
import os

assistant = VideoAssistant(
    use_api=True,
    api_key=os.getenv("GROQ_API_KEY"),  # Reads from environment
    api_provider="groq"
)
```

---

## Switching Between Local & API

You can easily switch modes:

```python
# Local Ollama (free, slower, needs GPU)
assistant_local = VideoAssistant(
    ollama_model="llama3.2:3b"
)

# Cloud API (paid, faster, any machine)
assistant_api = VideoAssistant(
    use_api=True,
    api_key=os.getenv("GROQ_API_KEY"),
    api_provider="groq"
)

# Both have the same API!
result = assistant_local.process_video("video.mp4")
result = assistant_api.process_video("video.mp4")
```

---

## Error Handling

### Invalid API Key
```python
try:
    assistant = VideoAssistant(use_api=True, api_key="invalid")
    result = assistant.process_video("video.mp4")
except Exception as e:
    if "401" in str(e):
        print("❌ Invalid API key! Check your key.")
```

### Rate Limit Exceeded
```python
try:
    result = assistant.process_video("video.mp4")
except Exception as e:
    if "429" in str(e):
        print("⏳ Rate limit exceeded! Wait a minute and try again.")
```

### Network Timeout
```python
assistant = VideoAssistant(
    use_api=True,
    api_key=api_key,
    api_provider="openai",
    timeout=120  # Increase if needed (default: 60 seconds)
)
```

---

## Troubleshooting

### "401 Unauthorized"
- ❌ Invalid API key
- ✅ Double-check your key (no extra spaces)
- ✅ Make sure you have credits (OpenAI/Anthropic)
- ✅ Check if key has expired

### "429 Too Many Requests"
- ❌ Rate limit exceeded
- ✅ Wait 60 seconds and try again
- ✅ Upgrade your API plan
- ✅ Use exponential backoff

### "Timeout"
- ❌ Network issue or API overloaded
- ✅ Check your internet connection
- ✅ Increase timeout parameter
- ✅ Try again in a few minutes

### "API request failed"
- ❌ General API error
- ✅ Check API status page
- ✅ Verify your account has quota/credits
- ✅ Try a different provider

---

## Performance Tips

1. **Use Groq for development**: FREE and super fast
2. **Use OpenAI GPT-4 for production**: Best quality
3. **Batch process videos**: Process multiple videos in parallel
4. **Cache results**: Save analysis results to avoid re-processing
5. **Use environment variables**: Never commit API keys to git

---

## Pricing Calculator

**Example costs for 100 videos (10 minutes each):**

- **Groq**: FREE (within rate limits)
- **OpenAI GPT-3.5**: $0.20 (very cheap!)
- **OpenAI GPT-4**: $2.00 (still cheap!)
- **Anthropic Claude**: $0.50

Compare with:
- **AWS GPU (g4dn.xlarge)**: $0.50/hour = $8-10 for 100 videos
- **Local GPU electricity**: ~$0.30/hour

**Cloud APIs are cheaper than running your own GPU!**

---

## Security Best Practices

### ✅ DO:
- Use environment variables for API keys
- Rotate keys regularly
- Use separate keys for dev/prod
- Monitor API usage dashboard
- Set spending limits

### ❌ DON'T:
- Commit API keys to git
- Share keys in screenshots
- Use same key across projects
- Store keys in plain text files
- Ignore usage alerts

---

## Need Help?

- **Groq Issues**: https://console.groq.com/docs
- **OpenAI Issues**: https://platform.openai.com/docs
- **Anthropic Issues**: https://docs.anthropic.com
- **Library Issues**: https://github.com/Aditya-Takawale/AI-Summary/issues

---

## Summary

**Quick Start (Copy & Paste):**

```python
import os
from ai_video_assistant import VideoAssistant

# Get free Groq key from https://console.groq.com
assistant = VideoAssistant(
    use_api=True,
    api_key=os.getenv("GROQ_API_KEY"),
    api_provider="groq",
    api_model="llama-3.1-8b-instant"
)

result = assistant.process_video("video.mp4")
print(result['summary'])
```

**That's it!** 🎉 You're processing videos 5-10x faster than local Ollama!
