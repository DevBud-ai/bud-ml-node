from pydantic import BaseModel
from typing import List, Optional


class AskLLMRequest(BaseModel):
    prompt: str
    api_key: str
    channel: Optional[str]='openai'
    model: Optional[str]='text-davinci-003'
    temperature: Optional[int]=0.8
    max_tokens: Optional[int]=256
    top_p: Optional[int]=1
    n: Optional[int]=1
    best_of: Optional[int]=1
