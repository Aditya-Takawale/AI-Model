"""
AI Video Assistant - Simple One-Command Processing

Just run: python process_video.py your_video.mp4

That's it! No complicated setup needed.
"""

import os
import sys
from dotenv import load_dotenv
from ai_video_assistant import VideoAssistant

# Load API key from .env file
load_dotenv()

def main():
    print("=" * 70)
    print("🎬 AI Video Assistant")
    print("=" * 70)
    
    # Check if video file is provided
    if len(sys.argv) < 2:
        print("\n❌ Error: No video file provided")
        print("\n📖 Usage:")
        print("   python process_video.py your_video.mp4")
        print("\n💡 Example:")
        print("   python process_video.py lecture.mp4")
        sys.exit(1)
    
    video_path = sys.argv[1]
    
    # Check if video exists
    if not os.path.exists(video_path):
        print(f"\n❌ Error: Video file not found: {video_path}")
        sys.exit(1)
    
    # Get API key from .env
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("\n❌ Error: GOOGLE_API_KEY not found!")
        print("\n📝 Please follow these steps:")
        print("   1. Open the .env file")
        print("   2. Add your Google API key:")
        print("      GOOGLE_API_KEY=your_key_here")
        print("\n🆓 Get a FREE API key at:")
        print("   https://makersuite.google.com/app/apikey")
        sys.exit(1)
    
    # Get settings from .env
    whisper_model = os.getenv("WHISPER_MODEL", "base")
    
    print(f"\n📹 Video: {video_path}")
    print(f"🤖 AI: Google Gemini 2.5 Flash")
    print(f"🎤 Transcription: Whisper ({whisper_model})")
    print(f"📂 Output: outputs/")
    print("\n⏳ Processing... This will take 2-3 minutes")
    print("=" * 70)
    print()
    
    try:
        # Initialize assistant
        assistant = VideoAssistant(
            whisper_model=whisper_model,
            use_api=True,
            api_key=api_key,
            api_provider="google",
            output_dir="outputs"
        )
        
        # Process video
        result = assistant.process_video(video_path)
        
        # Display results
        print("\n" + "=" * 70)
        print("✅ SUCCESS! Video processed successfully!")
        print("=" * 70)
        
        print("\n📊 SUMMARY:")
        print("-" * 70)
        print(result['summary'])
        
        print("\n💡 KEY INSIGHTS:")
        print("-" * 70)
        for i, insight in enumerate(result['insights'], 1):
            print(f"{i}. {insight}")
        
        print("\n📝 QUIZ:")
        print("-" * 70)
        for i, q in enumerate(result['quiz'], 1):
            print(f"\nQ{i}: {q['question']}")
            for key, opt in q['options'].items():
                marker = "✓" if key == q['correct_answer'] else " "
                print(f"  [{marker}] {key}. {opt}")
        
        # Get filename without extension
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        
        print("\n" + "=" * 70)
        print("📂 OUTPUT FILES:")
        print("=" * 70)
        print(f"📄 Analysis: outputs/{video_name}_analysis.docx")
        print(f"📝 Subtitles: outputs/{video_name}_subtitles.srt")
        print("=" * 70)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n🔍 Troubleshooting:")
        
        error_str = str(e)
        if "400" in error_str or "API_KEY_INVALID" in error_str:
            print("   ❌ Invalid API key")
            print("   📝 Get new key at: https://makersuite.google.com/app/apikey")
        elif "403" in error_str or "quota" in error_str.lower():
            print("   ❌ API quota exceeded")
            print("   ⏳ Wait a few minutes and try again")
        elif "404" in error_str:
            print("   ❌ Model not found or API not enabled")
            print("   📝 Enable API at: https://console.cloud.google.com/")
        else:
            print("   📝 Check: https://ai.google.dev/")
        
        sys.exit(1)


if __name__ == "__main__":
    main()
