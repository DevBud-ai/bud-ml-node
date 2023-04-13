from fastapi import FastAPI
import uvicorn
from llm.llm import get_openai_result
from models.api import AskLLMRequest


app = FastAPI()

@app.post("/ask-llm")
def ask_llm(requests: AskLLMRequest):
    
    return get_openai_result(requests)



def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8080, reload=True)