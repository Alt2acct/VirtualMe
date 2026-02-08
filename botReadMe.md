zeekbot/
├── Dockerfile              # Critical for Render
├── requirements.txt        # Python libraries
├── .env                    # Secrets (You create this)
├── main.py                 # The Master Controller
├── config.py               # Settings
│
├── core/
│   ├── __init__.py
│   ├── driver.py           # Selenium setup
│   └── bot.py              # The Logic (Bomb, DM, Listen)
│
├── brain/
│   ├── __init__.py
│   └── ai.py               # Connects to AI (Ollama or API)
│
├── database/
│   ├── __init__.py
│   └── storage.py          # Saves contacts & queues
│
└── dashboard/
    ├── templates/
    │   └── index.html      # The Control Panel
    └── static/
        └── style.css       # (Optional styling)
