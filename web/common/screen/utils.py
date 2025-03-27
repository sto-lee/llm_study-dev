from dotenv import load_dotenv
import os
from common.screen.history import init_history
from common.screen.display import print_history_message
from common.screen.input import choice_provider, choice_llms

def init_page():
    # .env 파일에 선언한 환경변수 등록
    load_dotenv()

    # 히스토리 초기화
    init_history()

def init_display():
    # 히스토리 메시지 표시
    print_history_message()

    # 프로바이더 선택
    choiced_provider = choice_provider()

    # 모델 선택
    choiced_llm = choice_llms(choiced_provider)
    return choiced_provider, choiced_llm