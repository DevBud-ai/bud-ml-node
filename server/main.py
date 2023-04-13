from fastapi import FastAPI
import uvicorn
from llm.llm import get_openai_result, get_replicate_result
from models.api import AskLLMRequest


app = FastAPI()

@app.post("/ask-llm")
def ask_llm(requests: AskLLMRequest):
    result = None
    if requests.channel is 'openai':
        result = get_openai_result(requests)
    else:
        result = get_replicate_result(requests)
    
    return result 



def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8080, reload=True)