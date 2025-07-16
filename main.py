import sys
from utils import extract_username, fetch_user_data
from persona_builder import build_persona
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python reddit_user_persona.py <reddit_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username(profile_url)
    if not username:
        print("Couldn't parse username from URL.")
        return 

    print(f"Fetching data for u/{username}...")
    comments, posts = fetch_user_data(username)
    print(f"Fetched {len(comments)} comments and {len(posts)} posts.")

    print("Building persona using local LLM...")
    persona_txt = build_persona(username, comments, posts)

    output_path = Path("personas") / f"{username}.txt"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(persona_txt, encoding="utf-8")
    print(f"Persona written to {output_path}")

if __name__ == "__main__":
    main()
