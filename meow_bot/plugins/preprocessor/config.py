from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    sudoers: list[str] = ["3493487882"]
