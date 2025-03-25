import streamlit as st 
from dotenv import load_dotenv 

load_dotenv() # .env 파일에 선언한 변수를 환경변수에 등록하는 함수 

from history import init_history, add_history
from display import print_history_message, print_message
from input import get_prompt, choice_llms
from common.llm.openai import get_response_from_llm, get_llm
from common.constant import ROLE_TYPE

st.title("Chatbot")

# 세션 상태 초기화
init_history() 
print_history_message()

# 사용자의 메세지 
choiced_llm = choice_llms()
prompt = get_prompt()

if prompt is not None:
    # 사용자 메시지를 세션 상태에 추가
    add_history(ROLE_TYPE.user, prompt)
    
    # 사용자 메시지 표시
    print_message(ROLE_TYPE.user.name, prompt)

    # AI 응답을 세션 상태에 추가
    with st.chat_message(ROLE_TYPE.assistant.name): # 채팅 메시지 영역 생성
        assistant_message = st.write_stream(get_response_from_llm(
            llm=get_llm(), messages=st.session_state.messages, llm_name=choiced_llm
        )) # 메시지 영역에 메시지를 차례대로 출력

    add_history(ROLE_TYPE.assistant, assistant_message)    
    # AI 응답 표시
    # print_message(ROLE_TYPE.assistant.name, assistant_message)

