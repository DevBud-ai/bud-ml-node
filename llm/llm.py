import os
import openai
from langchain.llms import OpenAI, Replicate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def get_template(type):
    
    if type == 'model_recognition':
        template = """
        I have a list of API's which generate text and image contents based on AI. Below are few of them.
        OpenAI - Helps to generate textual contents like blog, programming code, emails, etc
        Stable Diffusion - Helps to generate images based on the prompt
        MidJourney - Helps to generate images like midjourney
        Future Diffusion - Generate images with a futuristic Sci-Fi theme
        I want to identify which api to be used for fulfilling the below task.
        {query}
        Give a response in single word
        eg: Stable Diffusion
        """
    else:
        template = """{query}"""

    return template
    

def get_openai_result(params):
    """
    Method to get the OpenAI results
    """
    os.environ["OPENAI_API_KEY"] = params.openai_api_key
    
    template = get_template(params.type)
    print(template)
    prompt = PromptTemplate(
        input_variables=["query"],
        template=template
    )
    print(prompt.format(query=params.prompt))
    llm = OpenAI(model_name=params.model)
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(params.prompt)
    print(result)
    return result


def get_replicate_result(params):
    """
    Method to get the result from replicate
    """
    os.environ["REPLICATE_API_TOKEN"] = params.replicate_api_key
    text2image = Replicate(model=params.model, 
                       input={'image_dimensions': '512x512'})
    print(params.prompt)
    image_output = text2image(params.prompt)
    return image_output
