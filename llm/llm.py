import os
import openai
from langchain.llms import OpenAI, Replicate

def get_openai_result(params):
    """
    Method to get the OpenAI results
    """
    os.environ["OPENAI_API_KEY"] = params.api_key

    llm = OpenAI(model=params.model,
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
        n=params.n,
        best_of=params.best_of)
    result = llm(params.prompt)
    return result


def get_replicate_result(params):
    """
    Method to get the result from replicate
    """
    os.environ["REPLICATE_API_TOKEN"] = params.api_key
    text2image = Replicate(model=params.model, 
                       input={'image_dimensions': '512x512'})
    image_output = text2image(params.prompt)
    return image_output
