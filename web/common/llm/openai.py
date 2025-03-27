from openai import OpenAI
import enum
class OPENAI_LLMs(enum.Enum):
    gpt_4o_mini = (enum.auto(), "gpt-4o-mini") 
    gpt_4o = (enum.auto(), "gpt-4o") 

def clientOpenAI(model, messages, stream=True):
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    return response
