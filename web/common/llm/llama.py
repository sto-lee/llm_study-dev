from groq import Groq
import enum
import time
class GROQ_LLMs(enum.Enum):
    gemma2_9b_it = (enum.auto(), "gemma2-9b-it") 
    llama_3_3_70b_versatile = (enum.auto(), "llama-3.3-70b-versatile") 
    llama_3_1_8b_instant = (enum.auto(), "llama-3.1-8b-instant") 
    llama_3_8b_8192 = (enum.auto(), "llama3-8b-8192") 

def clientGroq(model, messages, stream=True):
    client = Groq()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    return response


