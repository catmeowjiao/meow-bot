from pydantic import Extra, BaseModel
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    openai_api_key: Optional[
        str
    ] = "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"
    openai_model_name: Optional[str] = "gpt-3.5-turbo"
    openai_max_history_limit: Optional[int] = 30
    openai_http_proxy: Optional[str] = None
    enable_private_chat: bool = True
    chatgpt_turbo_public: bool = False


class ConfigError(Exception):
    pass
