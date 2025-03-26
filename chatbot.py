import streamlit as st 

from common.screen.utils import init_page, init_display
from common.screen.history import add_history
from common.screen.display import print_message
from common.screen.input import get_prompt
from common.llm.call_provider import get_response_from_llm
from common.llm.provider_type import PROVIDER_TYPE
from common.screen.constant import ROLE_TYPE

st.title("Chatbot")

# 페이지 초기화
init_page()

# 화면 초기화
choiced_provider, choiced_llm = init_display()

prompt = get_prompt()

if prompt is not None:
    # 사용자 메시지를 세션 상태에 추가
    add_history(ROLE_TYPE.user, prompt)
    
    # 사용자 메시지 표시
    print_message(ROLE_TYPE.user.name, prompt)

    assistant_message = print_message(ROLE_TYPE.assistant.name, 
                get_response_from_llm(PROVIDER_TYPE[choiced_provider],
                                    messages=st.session_state.messages,
                                    llm_name=choiced_llm))

    # AI 응답을 세션 상태에 추가
    add_history(ROLE_TYPE.assistant, assistant_message)

