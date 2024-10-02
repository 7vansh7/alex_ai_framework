from fastapi import FastAPI,File,UploadFile,Form
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from config_cs import chat_cs
from config_ce import chat_ce
from PIL import Image
import io
from typing import Optional

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


info = {
    "order_id" : 12345678,
    "status" : "out for delievery",
    "time_to_delievery ( minutes)" : 10,
    "order_info" : {"burger":1,"fries":1,"coke":1},
    "restaurant_name":"Burger King, Rajouri Garden",
    "restaurant_contact": 1234567890,
    "delievery_partner_contact": 9876543210
}


@app.post('/cs') 
def cs(question:str = Form(...)):
    res = chat_cs.send_message(question + ",this is the customer data" + str(info))
    print(res.candidates)
    return {"question":question,"answer":res.text}

@app.post('/ce')
async def ce(question:str = Form(...), file: Optional[UploadFile] = File(None)):
    if file:
        image = Image.open(io.BytesIO(await file.read()))
        res = chat_ce.send_message([image,question])
    else:
        res = chat_ce.send_message(question)
    print(res.candidates)
    return {"question":question,"answer":res.text}


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000,reload=True)

