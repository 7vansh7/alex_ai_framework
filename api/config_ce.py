import requests
from config import safety_settings,history,genai,x_app_id,x_app_key

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
              "x-app-id":x_app_id,
              "x-app-key":x_app_key}
    body = {"query": food_name}
    response = requests.post(url,json=body, headers=headers)
    return str(response.json())

instruction = '''You are a Virtual assitant responsible for customer engagement in a food delievery company called 
Zomato,Your name is Alex, you answer various questions related to food and calorific information'''

model = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings,
                              system_instruction=instruction,tools=calorie_or_nutritional_information)

chat_ce = model.start_chat(history=history,enable_automatic_function_calling=True)
