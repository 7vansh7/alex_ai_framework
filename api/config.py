import google.generativeai as genai
from dotenv import load_dotenv
import os 

load_dotenv()

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  }
]

x_app_id = os.getenv('NUTRITIONIX_X_APP_ID')
x_app_key = os.getenv('NUTRITIONIX_X_APP_KEY')

history = []

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
