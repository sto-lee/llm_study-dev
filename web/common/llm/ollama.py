import enum
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

class OLLAMA_LLMs(enum.Enum):
    gemma3_1b = (enum.auto(), "gemma3:1b") 
    gemma3_12b = (enum.auto(), "gemma3:12b") 
    exaone_deep_32b = (enum.auto(), "exaone-deep-32b") 
    exaone_deep_7b = (enum.auto(), "exaone-deep-7b") 

def create_ollama_prompt_template(messages):
    return ChatPromptTemplate.from_messages([
        *[{"role": msg["role"], "content": msg["content"]} for msg in messages]
    ])

def clientOllama(model, messages, stream=True):
    client = ChatOllama(model=model, stream=stream)
    chat_prompt = create_ollama_prompt_template(messages)
    chain = chat_prompt | client | StrOutputParser()
    response = chain.stream({})
    return response