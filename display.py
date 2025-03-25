import streamlit as st 

def print_message(role, message):
  with st.chat_message(role):
    st.markdown(message)

def print_history_message():
  # 이전 대화 내역을 화면에 표시
  for message in st.session_state.messages:
    print_message(message["role"], message["content"])


