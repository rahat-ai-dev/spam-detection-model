from fastapi import FastAPI
from pydantic import BaseModel
from src.models.predict import predict_message

app=FastAPI(
    title='Spam Detection API',
    description='SMS spam detection using ML',
    version='1.0.0'
)

class Message(BaseModel):
    text: str

@app.get('/')
def predict(msg:Message):
    return {'message':'Spam Detection API is running!'}

@app.post("/predict")
def predict(msg:Message):
    result=predict_message(msg.text)
    return {
        'text':msg.text,
        "prediction": result,
        "is_spam": result=="Spam"
        
    }
