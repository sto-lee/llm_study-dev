import streamlit as st
from common.llm.openai import OPENAI_LLMs


def get_prompt():
  return st.chat_input("무엇이든지 물어봐주세요.")


def choice_llms():
  choiced_llm = st.sidebar.selectbox(
    label="모델을 선택해주세요.",
    options=list(OPENAI_LLMs.__members__)
  )

  return choiced_llm

