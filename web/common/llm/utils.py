import time
from common.llm.provider_type import PROVIDER_TYPE

def generator_response(response, provider):
    if provider == PROVIDER_TYPE.ollama:
        for token in response:
            yield token  # Ollama는 이미 문자열을 반환
    else:
        for token in response:
            if token.choices[0].delta.content is not None:
                yield token.choices[0].delta.content
                time.sleep(0.05)