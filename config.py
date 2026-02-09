import os
from dotenv import load_dotenv

load_dotenv()

# RENDER_DISK_PATH should be set to /var/data in Render Dashboard if you add a Disk.
# Otherwise it defaults to local ./data
DATA_DIR = os.getenv("RENDER_DISK_PATH", "./data")

# Make sure directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

CHROME_SESSION_DIR = os.path.join(DATA_DIR, "chrome_session")
DB_FILE = os.path.join(DATA_DIR, "zeekbot.json")
QR_CODE_PATH = os.path.join(DATA_DIR, "qrcode.png")

# AI Settings (Use 'ollama' or 'groq'/'openai')
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama") 
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_MODEL_NAME = os.getenv("AI_MODEL_NAME", "llama3")
