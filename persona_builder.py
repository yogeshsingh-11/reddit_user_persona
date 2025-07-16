import requests

OLLAMA_API = "http://localhost:11434/api/generate"

def build_persona(username, comments, posts):
    combined = (comments + posts)[:30]
    examples = "\n".join([f"- \"{text[:200].replace('\"','')}...\" (Source: {link})" for text, link in combined])

    prompt = f"""
You are an analyst. Here's Reddit content by u/{username}:

{examples}

Generate a user persona including:
- Interests
- Personality traits
- Writing style
- Any profession/hobbies
- Political/religious views (if present)

For each trait, include a bullet with:
- A short description
- A citation in parentheses linking to the source (the Reddit URL)
"""

    resp = requests.post(OLLAMA_API, json={
        "model": "mistral",
        "prompt": prompt,
        "max_tokens": 800,
        "temperature": 0.7
    })
    resp.raise_for_status()
    return resp.json()["response"]
