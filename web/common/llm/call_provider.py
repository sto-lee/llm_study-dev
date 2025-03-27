from common.llm.utils import generator_response
from common.llm.provider_type import PROVIDER_TYPE

def get_response_from_llm(choiced_provider:str, messages, llm_name:str):
    if not isinstance(choiced_provider, PROVIDER_TYPE):
        raise Exception("제공자명이 아닙니다.")
    elif llm_name not in choiced_provider.value[2]:
        raise Exception("허락한 모델명이 아닙니다.") 

    response = choiced_provider.value[1](choiced_provider.value[2][llm_name].value[1],
                                        messages,
                                        stream=True)

    return generator_response(response, choiced_provider)