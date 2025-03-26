import streamlit as st 
from dotenv import load_dotenv 

load_dotenv() # .env 파일에 선언한 변수를 환경변수에 등록하는 함수 

from common.screen.history import init_history, add_history
from common.screen.display import print_history_message, print_message
from common.screen.input import get_prompt, choice_llms, choice_provider
from common.llm.call_provider import PROVIDER_TYPE, get_response_from_llm
from common.screen.constant import ROLE_TYPE

st.title("Chatbot")

# 세션 상태 초기화
init_history() 
print_history_message()

# 사용자의 메세지 
choiced_provider = choice_provider()
choiced_llm = choice_llms(choiced_provider)
prompt = get_prompt()

if prompt is not None:
    # 사용자 메시지를 세션 상태에 추가
    add_history(ROLE_TYPE.user, prompt)
    
    # 사용자 메시지 표시
    print_message(ROLE_TYPE.user.name, prompt)

    assistant_message = print_message(ROLE_TYPE.assistant.name, 
                get_response_from_llm(PROVIDER_TYPE[choiced_provider], messages=st.session_state.messages, llm_name=choiced_llm),
                is_streaming=True)

    # AI 응답을 세션 상태에 추가
    add_history(ROLE_TYPE.assistant, assistant_message)    
    # AI 응답 표시
    # print_message(ROLE_TYPE.assistant.name, assistant_message)

