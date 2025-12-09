"""OpenRouter API configuration for LangGraph agent."""
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "llama-3.3-70b-versatile"

ALLOWED_CATEGORIES = ["fashion", "electronics", "home", "beauty", "sports", "food", "books", "other"]
ALLOWED_CONDITIONS = ["new", "used", "refurbished"]