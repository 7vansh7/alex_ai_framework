import google.generativeai as genai
import requests

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

calorie_or_nutritional_information = {'function_declarations': [
      {'name': 'calorie_or_nutritional_information',
       'description': '''returns the calorific breakdown and nutritional information data about a food item
       like calories,protein,carbohydrates''',
       'parameters': {'type_': 'OBJECT',
       'properties': {
         'a': {'type_': 'STRING'}
       },
       'required': ['a']} }]}

genai.protos.Tool(calorie_or_nutritional_information)

def calorie_or_nutritional_information(food_name:str):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {"Content-Type": "application/json",
              "x-app-id":"4031d7ed",
              "x-app-key":"77c515afe6b2c5fd3dfba64d0c005213"}
    body = {"query": food_name}
    response = requests.post(url,json=body, headers=headers)
    return str(response.json())

instruction = '''You are a Virtual assitant responsible for customer engagement in a food delievery company called 
Zomato,Your name is Alex, you answer various questions related to food and calorific information'''

history = []


genai.configure(api_key='AIzaSyAxDlqSHz9f7MjpWngTe_hKiMBEbtowbMU')


model = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings,
                              system_instruction=instruction)

chat_ce = model.start_chat(history=history)
