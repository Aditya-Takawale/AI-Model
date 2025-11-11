"""
Production-ready video processing script with API support
Works on Windows, macOS, Linux, and servers

Usage:
    python process_with_api.py video.mp4
    python process_with_api.py video.mp4 --provider groq
    python process_with_api.py video.mp4 --provider openai --model gpt-4

Environment variables (set in .env file):
    GROQ_API_KEY=gsk_...
    OPENAI_API_KEY=sk_...
    ANTHROPIC_API_KEY=sk-ant_...
    XAI_API_KEY=xai_...
"""

import os
import sys
import argparse
from dotenv import load_dotenv
from ai_video_assistant import VideoAssistant

# Load environment variables from .env file
load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description="Process video with AI transcription and analysis"
    )
    parser.add_argument("video", help="Path to video file")
    parser.add_argument(
        "--provider",
        choices=["groq", "openai", "anthropic", "xai", "google"],
        default=os.getenv("API_PROVIDER", "groq"),
        help="API provider to use (default: groq)"
    )
    parser.add_argument(
        "--model",
        help="Model name (optional, uses provider default if not specified)"
    )
    parser.add_argument(
        "--whisper-model",
        default=os.getenv("WHISPER_MODEL", "base"),
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size (default: base)"
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Output directory (default: outputs)"
    )
    
    args = parser.parse_args()
    
    # Get API key from environment
    api_key_map = {
        "groq": "GROQ_API_KEY",
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "xai": "XAI_API_KEY",
        "google": "GOOGLE_API_KEY"
    }
    
    env_var = api_key_map[args.provider]
    api_key = os.getenv(env_var)
    
    if not api_key:
        print(f"❌ Error: {env_var} not found in environment")
        print(f"\nPlease set your API key:")
        print(f"  1. Copy .env.example to .env")
        print(f"  2. Add your API key: {env_var}=your_key_here")
        print(f"  3. Get a free key at: https://console.{args.provider}.com")
        sys.exit(1)
    
    if not os.path.exists(args.video):
        print(f"❌ Error: Video file not found: {args.video}")
        sys.exit(1)
    
    print("=" * 70)
    print("🎬 AI Video Assistant - Production Mode")
    print("=" * 70)
    print(f"📹 Video: {args.video}")
    print(f"🤖 Provider: {args.provider.upper()}")
    if args.model:
        print(f"📦 Model: {args.model}")
    print(f"🎤 Whisper: {args.whisper_model}")
    print(f"📂 Output: {args.output_dir}")
    print("=" * 70)
    print()
    
    try:
        # Initialize assistant
        assistant = VideoAssistant(
            whisper_model=args.whisper_model,
            use_api=True,
            api_key=api_key,
            api_provider=args.provider,
            api_model=args.model,
            output_dir=args.output_dir
        )
        
        # Process video
        result = assistant.process_video(args.video)
        
        # Display results
        print("\n" + "=" * 70)
        print("✅ SUCCESS!")
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
        
        print("\n" + "=" * 70)
        print("📂 Output Files:")
        print("=" * 70)
        print(f"  • Subtitles: {result.get('subtitle_file', 'N/A')}")
        print(f"  • Analysis: {result.get('analysis_file', 'N/A')}")
        print(f"  • Video: {result.get('video_with_subtitles', 'N/A')}")
        print("=" * 70)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check your API key is valid")
        print("2. Verify you have API credits/quota")
        print("3. Check your internet connection")
        print(f"4. Visit https://console.{args.provider}.com for help")
        sys.exit(1)


if __name__ == "__main__":
    main()
