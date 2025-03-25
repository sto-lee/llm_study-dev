from openai import OpenAI
import enum

class OPENAI_LLMs(enum.Enum):
  gpt_4o_mini = (enum.auto(), "gpt-4o-mini") 
  gpt_4o = (enum.auto(), "gpt-4o") 


def get_llm():
  return OpenAI()

def get_response_from_llm(llm, messages, llm_name:str):
  if llm_name not in OPENAI_LLMs.__members__:
    raise Exception("허락한 OpenAI 모델명이 아닙니다.") 

  # 전체 대화 내역을 OpenAI에 전달
  response = llm.chat.completions.create(
      model=OPENAI_LLMs[llm_name].value[1], # "gpt-4o-mini"
      messages=messages
  )

  return response.choices[0].message.content

