import json
from nonebot import get_driver
from nonebot.message import event_preprocessor
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.log import logger
from .config import Config

config = Config.parse_obj(get_driver().config)


@event_preprocessor
async def _(event: MessageEvent):
    for command_start in get_driver().config.command_start:
        if event.get_plaintext().startswith(f"{command_start}sudo"):
            file = open("data/blacklist.json", "r")
            file_data = file.read()
            file.close()
            blacklist = json.loads(file_data)
            if (
                event.get_user_id() in list(config.sudoers)
                and event.get_plaintext().strip().split(" ")[1] not in blacklist["data"]
            ):
                event.user_id = event.user_id = int(
                    event.get_plaintext().strip().split(" ")[1]
                )
                cmd_start = command_start if config.sudo_insert_cmdstart else ""
                event.message[0].data["text"] = cmd_start + " ".join(
                    event.message[0].data["text"].split(" ")[2:]
                )
