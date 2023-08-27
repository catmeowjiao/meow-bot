from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    sudoers: list[str] = ["3493487882", "2920571540"]
    sudo_insert_cmdstart: int = 0
