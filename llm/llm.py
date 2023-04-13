import os
import openai
from langchain.llms import OpenAI

def get_openai_result(params):
    """
    Method to get the OpenAI results
    """
    os.environ["OPENAI_API_KEY"] = params.open_api_key

    llm = OpenAI(model=params.model,
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
        n=params.n,
        best_of=params.best_of)
    result = llm(params.prompt)
    return result