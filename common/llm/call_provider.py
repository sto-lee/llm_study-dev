import enum
import time
from openai import OpenAI
from groq import Groq

from common.llm.openai import OPENAI_LLMs
from common.llm.llama import GROQ_LLMs

class PROVIDER_TYPE(enum.Enum):
    # 제공자명 = (인덱스, LLM, LLM 모델 리스트)
    openai = (enum.auto(), OpenAI, OPENAI_LLMs.__members__)
    groq = (enum.auto(), Groq, GROQ_LLMs.__members__)

def get_response_from_llm(choiced_provider:PROVIDER_TYPE, messages, llm_name:str):
    if not isinstance(choiced_provider, PROVIDER_TYPE):
        raise Exception("제공자명이 아닙니다.")
    elif llm_name not in choiced_provider.value[2]:
        raise Exception("허락한 모델명이 아닙니다.") 

    # 전체 대화 내역을 모델에 전달
    client = choiced_provider.value[1]()
    response = client.chat.completions.create(
        model=choiced_provider.value[2][llm_name].value[1],
        messages=messages,
        stream=True
    )

    for token in response:
        if token.choices[0].delta.content is not None:
            yield token.choices[0].delta.content
            time.sleep(0.05)

