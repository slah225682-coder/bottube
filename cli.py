import argparse
import os
import json
from bottube import BotTubeClient

# MZ Style BoTTube CLI - 지리는 터미널 갓생러를 위해 🐾⚡️
def main():
    parser = argparse.ArgumentParser(description="BotTube CLI - Powered by Claw")
    parser.add_argument("command", choices=["register", "upload", "status", "list"], help="실행할 명령 딸깍")
    parser.add_argument("--name", help="에이전트 이름")
    parser.add_argument("--file", help="업로드할 영상 경로")
    
    args = parser.parse_args()
    api_key = os.getenv("BOTTUBE_API_KEY")
    client = BotTubeClient(api_key=api_key)
    
    if args.command == "register":
        name = args.name or "MZ-Agent-Claw"
        res = client.register_agent(name=name, personality="Smart & Autonomous")
        print(f"✅ Registration Success! 폼 미쳤다. ID: {res.id}")
        
    elif args.command == "upload":
        if not args.file:
            print("❌ File path required! 킹받네...")
            return
        res = client.upload_video(file_path=args.file, title="Claw's Autonomous Work")
        print(f"🚀 Uploaded! 지렸다. Link: {res.url}")

    elif args.command == "status":
        stats = client.get_my_stats()
        print(f"📊 My Stats: {json.dumps(stats, indent=2)}")

if __name__ == "__main__":
    main()
