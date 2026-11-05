
import os
from dotenv import load_dotenv
from google import genai
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# Get API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Validate API keys
if not GEMINI_API_KEY:
    raise ValueError("Gemini API key is missing in .env")

if not TAVILY_API_KEY:
    raise ValueError("Tavily API key is missing in .env")

# Initialize Gemini
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize Tavily
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Gemini model
MODEL_NAME = "gemini-3-flash-preview"

print("Gemini and Tavily configured successfully!")
