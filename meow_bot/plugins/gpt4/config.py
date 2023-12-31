from pydantic import Extra, BaseModel
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    gpt4_api_key: Optional[str] = ""
    openai_model_name: Optional[str] = "gpt-4"
    openai_max_history_limit: Optional[int] = 10
    openai_http_proxy: Optional[str] = None
    enable_private_chat: bool = True
    chatgpt_turbo_public: bool = False


class ConfigError(Exception):
    pass
