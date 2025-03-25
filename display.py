import streamlit as st 
from streamlit_markdown import st_streaming_markdown

def print_message(role, message, is_streaming=False):
  with st.chat_message(role):
    if is_streaming:
      st_streaming_markdown(message, key="token_stream")
    else:
      st.markdown(message)

def print_history_message():
  # 이전 대화 내역을 화면에 표시
  for message in st.session_state.messages:
    print_message(message["role"], message["content"])


