import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not found in environment variables.")

CATEGORIES_FILE = "data/categories.xlsx"

CONFIDENCE_THRESHOLD = 85 #in percentage

OPENAI_MODEL = "gpt-5-nano" # Need to check if this is the right model

if __name__ == "__main__":
    print("Config loaded successfully.")
    print("API Key exists:", OPENAI_API_KEY is not None)

