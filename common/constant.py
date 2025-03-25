import enum 

class ROLE_TYPE(enum.Enum):
  user = (enum.auto(), "user")
  assistant = (enum.auto(), "assistant")
  system = (enum.auto(), "system")

class HISTORY_INFO(enum.Enum):
  role = (enum.auto(), "role")
  content = (enum.auto(), "content")
