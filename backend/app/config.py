import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from root directory
load_dotenv()

# === OpenAI Settings ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

# === Logging Settings ===
# Default: logs to data/interactions.jsonl
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "../data/interactions.jsonl")

# === Application Mode ===
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"
