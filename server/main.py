from typing import Tuple

from fastapi import FastAPI, HTTPException
import uvicorn

from llm.llm import get_openai_result, get_replicate_result
from models.api import AskLLMRequest

app = FastAPI()


def get_model_name(model_id: str) -> Tuple[str, str]:
    stable_arr = ["Stable Diffusion", "StableDiffusion", "stable diffusion"]
    midj_arr = ["MidJourney", "Mid Journey", "MidJorney"]
    
    if model_id == "OpenAI":
        model_name = "text-davinci-003"
        model_type = "openai"
    elif model_id in stable_arr:
        model_name = "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"
        model_type = "replicate"
    elif model_id in midj_arr:
        model_name = "prompthero/openjourney:9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb"
        model_type = "replicate"
    elif model_id in ["Future Diffusion", "FutureDiffusion", "futurediffusion"]:
        model_name = "cjwbw/future-diffusion:b5c46a3b3f0db2a154d4be534ba7758caded970b748a2e26e6d02e9b3bd7da2a"
        model_type =  "replicate"
    else:
        model_name = "na"
        model_type = "na"
    
    return model_name, model_type


@app.post("/ask-llm")
def ask_llm(requests: AskLLMRequest):
    requests.type = 'model_recognition'
    
    # Get model_identified from OpenAI
    model_identified = get_openai_result(requests)
    
    # Clean up model_identified string
    model_identified = model_identified.replace("\n", "").replace(".", "").replace(" ", "")
    
    print("model_identified", model_identified)
    
    # Get model_name and model_type
    model_name, model_type = get_model_name(model_identified)
    
    print(model_name, model_type)
    
    if model_type == "openai":
        requests.model = model_name
        requests.type = ''
        result = get_openai_result(requests)
    elif model_type == "replicate":
        requests.model = model_name
        if not requests.replicate_api_key:
            raise HTTPException(status_code=422, detail="To process this request, a Replicate API token is required")
        result = get_replicate_result(requests)
    else:
        raise HTTPException(status_code=400, detail="Unable to identify the right model to process this request")
    
    return {
        "model_identified": model_identified,   
        "result": result
    }


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=9080, reload=True)
