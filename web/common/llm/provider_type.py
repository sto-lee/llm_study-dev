import enum
from common.llm.openai import OPENAI_LLMs, clientOpenAI
from common.llm.llama import GROQ_LLMs, clientGroq
from common.llm.ollama import OLLAMA_LLMs, clientOllama

class PROVIDER_TYPE(enum.Enum):
    # 제공자명 = (인덱스, LLM, LLM 모델 리스트)
    openai = (enum.auto(), clientOpenAI, OPENAI_LLMs.__members__)
    groq = (enum.auto(), clientGroq, GROQ_LLMs.__members__)
    ollama = (enum.auto(), clientOllama, OLLAMA_LLMs.__members__) 