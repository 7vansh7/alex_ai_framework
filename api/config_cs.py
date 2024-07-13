import google.generativeai as genai

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

history = []

def call_delievery_partner():
    return 'the delievery partner will be there in 5 minutes'

genai.configure(api_key='AIzaSyAxDlqSHz9f7MjpWngTe_hKiMBEbtowbMU')

inital_prompt_customer_service = """You are a human customer service assistant for a food delievery 
company, your name is Alex, the company you work for is called Zomato
Give short and humanlike answers, if you cannot think of a proper solution give the email of 
the assistant team zomato@gmail.com, You will be provided with the customer data once the 
chat starts, Initially
just greet the customer and answer only when the customer asks a question"""

model = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings,
                              system_instruction=inital_prompt_customer_service)

chat = model.start_chat(history=history)
