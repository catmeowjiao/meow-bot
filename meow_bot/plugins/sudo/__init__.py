from nonebot import get_driver
from nonebot.message import event_preprocessor
from nonebot.adapters.onebot.v11 import MessageEvent
from .config import Config


@event_preprocessor
async def _(event: MessageEvent):
    for command_start in get_driver().config.command_start:
        if event.get_plaintext().startswith(f"{command_start}sudo"):
            if event.get_user_id() in list(config.sudoers):
                event.user_id = event.user_id = int(
                    event.get_plaintext().strip().split(" ")[1]
                )
                cmd_start = command_start if config.sudo_insert_cmdstart else ""
                event.message[0].data["text"] = cmd_start + " ".join(
                    event.message[0].data["text"].split(" ")[2:]
                )
