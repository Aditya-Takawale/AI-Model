"""
Example: Using AI Video Assistant with Cloud API (OpenAI/Groq/Anthropic)

This example shows how to use cloud APIs instead of local Ollama.
Perfect for servers without GPU or when you need faster processing.

Costs (approximate per 10-min video):
- OpenAI GPT-3.5: ~$0.002 (very cheap!)
- OpenAI GPT-4: ~$0.02 
- Groq (Llama 3.1): FREE (with rate limits)
- Anthropic Claude: ~$0.005

Speed:
- OpenAI: 2-4 seconds
- Groq: 1-2 seconds (VERY FAST!)
- Anthropic: 3-5 seconds
"""

import ssl
import os

# SSL bypass for Whisper (if needed on Mac)
# ssl._create_default_https_context = ssl._create_unverified_context

from ai_video_assistant import VideoAssistant

# ============================================================
# CONFIGURATION
# ============================================================

# Option 1: OpenAI (Most reliable, small cost)
API_PROVIDER = "openai"
API_KEY = "sk-your-openai-key-here"  # Get from https://platform.openai.com/api-keys
API_MODEL = "gpt-3.5-turbo"  # or "gpt-4" for better quality

# Option 2: Groq (FREE, VERY FAST!)
# API_PROVIDER = "groq"
# API_KEY = "gsk_your-groq-key-here"  # Get from https://console.groq.com
# API_MODEL = "llama-3.1-8b-instant"

# Option 3: Anthropic Claude (Good quality)
# API_PROVIDER = "anthropic"
# API_KEY = "sk-ant-your-anthropic-key-here"  # Get from https://console.anthropic.com
# API_MODEL = "claude-3-haiku-20240307"

# Or use environment variable (recommended for security)
# API_KEY = os.getenv("OPENAI_API_KEY")  # Set with: export OPENAI_API_KEY=sk-...

# ============================================================
# PROCESS VIDEO
# ============================================================

print("🎬 AI Video Assistant - API Mode")
print("=" * 60)
print(f"📡 Provider: {API_PROVIDER.upper()}")
print(f"🤖 Model: {API_MODEL}")
print("=" * 60 + "\n")

# Initialize with API mode
assistant = VideoAssistant(
    whisper_model="base",      # Local Whisper (always runs locally)
    use_api=True,              # Use cloud API instead of Ollama
    api_key=API_KEY,           # Your API key
    api_provider=API_PROVIDER, # "openai", "groq", or "anthropic"
    api_model=API_MODEL        # Specific model to use
)

# Process video
video_path = "./test_videos/test_video_1.mp4"
print(f"🎥 Processing: {video_path}\n")

try:
    result = assistant.process_video(video_path)
    
    # Display results
    print("\n" + "=" * 60)
    print("VIDEO LECTURE ANALYSIS RESULTS")
    print("=" * 60 + "\n")
    
    print("SUMMARY:")
    print("-" * 60)
    print(result['summary'])
    print()
    
    print("KEY INSIGHTS:")
    print("-" * 60)
    for i, insight in enumerate(result['insights'], 1):
        print(f"{i}. {insight}")
    print()
    
    print("QUIZ QUESTIONS:")
    print("-" * 60)
    for i, question in enumerate(result['quiz'], 1):
        if i > 1:
            print()
        
        print(f"Question {i}: {question['question']}")
        
        options = question['options']
        if isinstance(options, dict):
            for key, option_text in options.items():
                is_correct = key == question['correct_answer']
                marker = "[✓]" if is_correct else "[ ]"
                print(f"  {marker} {key}. {option_text}")
    
    print("\n" + "=" * 60)
    print("Analysis completed successfully!")
    print("=" * 60)
    print(f"\n📂 Output files:")
    print(f"   - Subtitles: outputs/{os.path.basename(video_path).replace('.mp4', '_subtitles.srt')}")
    print(f"   - Analysis: outputs/{os.path.basename(video_path).replace('.mp4', '_analysis.docx')}")

except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    print("\nTroubleshooting:")
    print("1. Check your API key is valid")
    print("2. Verify you have API credits/quota")
    print("3. Check your internet connection")
    print(f"4. Visit https://platform.{API_PROVIDER}.com to manage your account")
