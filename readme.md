
# 🧠 Reddit User Persona Builder

This project builds a **detailed user persona** by scraping a Reddit profile's public posts and comments and summarizing them using a local open-source LLM (Mistral via [Ollama](https://ollama.com)).

---

## 📌 Features

- Scrapes **posts and comments** of any Reddit user
- Generates a **detailed user persona** using a local open-source LLM
- **Cites each trait** with links to the supporting post or comment
- Outputs clean, readable `.txt` files in the `personas/` folder
- Fully **PEP-8** compliant, modular and extensible

---

## 🧰 Tech Stack

- **Python 3.10+**
- **PRAW** – Reddit API Wrapper
- **Ollama** – Local LLM API Runtime
- **Mistral** – Open-source LLM used for persona generation
- **dotenv, requests, tqdm** – Utilities

---

## 🛠️ Setup Instructions

### 1. 🧬 Clone and Install Dependencies

```bash
git clone https://github.com/yourusername/reddit-user-persona.git
cd reddit-user-persona
python -m venv venv
source venv/bin/activate        # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 🔐 Configure Reddit API

Create a Reddit app at: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

Then create a `.env` file in your project root:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=reddit-persona-script
```

You can also use `.env.example` as a template.

### 3. 🧠 Install & Run Ollama + Mistral

Install [Ollama](https://ollama.com) and pull the Mistral model:

```bash
ollama pull mistral
ollama serve
```

This will serve the model on `http://localhost:11434`.

---

## 🚀 Usage

Once setup is complete, run the script with any Reddit profile URL:

```bash
python reddit_user_persona.py https://www.reddit.com/user/kojied/
```

- This fetches and analyzes the user’s comments and posts.
- A persona is generated and saved in:

```
personas/kojied.txt
```

Try with another user:

```bash
python reddit_user_persona.py https://www.reddit.com/user/Hungry-Move-6603/
```

You can open the `.txt` file for a detailed breakdown of interests, personality traits, etc.

---

## 📂 Project Structure

```
reddit_user_persona/
├── reddit_user_persona.py       # Main script to execute
├── utils.py                     # Reddit scraping functions
├── persona_builder.py           # Uses Mistral LLM to generate persona
├── personas/                    # Output directory for persona files
├── .env                         # Reddit API credentials (NOT committed)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 📋 Sample Output (`personas/kojied.txt`)

```
u/kojied — User Persona

1. Interests:
- Strategy Games (e.g., Manor Lords)
  > “Each family will eat each type of food equally...” (Source: [link])

2. Personality:
- Thoughtful, curious, and introspective...

3. Writing Style:
- Clear and reflective

...
```

Each point includes citations with links to the source posts/comments.

---

## ✅ Code Quality

To ensure PEP-8 compliance:

```bash
black .
flake8
```

---

## 🤝 License

This project is licensed under the MIT License.

---

