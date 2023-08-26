import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Message, MessageEvent, GroupMessageEvent
from nonebot.message import event_preprocessor
from nonebot.exception import IgnoredException
from nonebot.permission import SUPERUSER
from nonebot import get_driver
from nonebot.message import event_preprocessor
from .config import Config

config = Config.parse_obj(get_driver().config)


@event_preprocessor
async def _(bot: Bot, event: MessageEvent):
    sudo = False
    for command_start in get_driver().config.command_start:
        if event.get_plaintext().startswith(f"{command_start}sudo"):
            if event.get_user_id() in list(config.sudoers):
                sudo = True
                event.user_id = int(event.get_plaintext().strip().split(" ")[1])
                cmd_start = command_start if config.sudo_insert_cmdstart else ""
                event.message[0].data["text"] = cmd_start + " ".join(
                    event.message[0].data["text"].split(" ")[2:]
                )
    if isinstance(event, GroupMessageEvent):
        for command_start in get_driver().config.command_start:
            if event.get_user_id() == "3493487882":
                if event.get_plaintext().startswith(f"{command_start}sm"):
                    file = open("../meow-bot/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id in file_dict["data"]:
                        file_dict["data"].remove(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    file = open("../meow-bot-2/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id not in file_dict["data"]:
                        file_dict["data"].append(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot-2/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    await bot.send_group_msg(group_id=event.group_id, message="切换成功")
                elif event.get_plaintext().startswith(f"{command_start}sd"):
                    file = open("../meow-bot/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id not in file_dict["data"]:
                        file_dict["data"].append(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    file = open("../meow-bot-2/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id in file_dict["data"]:
                        file_dict["data"].remove(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot-2/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    await bot.send_group_msg(group_id=event.group_id, message="切换成功")
                elif event.get_plaintext().startswith(f"{command_start}ea"):
                    file = open("../meow-bot/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id in file_dict["data"]:
                        file_dict["data"].remove(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    file = open("../meow-bot-2/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id in file_dict["data"]:
                        file_dict["data"].remove(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot-2/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    await bot.send_group_msg(group_id=event.group_id, message="启用成功")
                elif event.get_plaintext().startswith(f"{command_start}sm"):
                    file = open("../meow-bot/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id not in file_dict["data"]:
                        file_dict["data"].append(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    file = open("../meow-bot-2/data/node.json", "r")
                    file_data = file.read()
                    file.close()
                    file_dict = json.loads(file_data)
                    if event.group_id not in file_dict["data"]:
                        file_dict["data"].append(event.group_id)
                    file_data = json.dumps(file_dict)
                    file = open("../meow-bot-2/data/node.json", "w")
                    file.write(file_data)
                    file.close()
                    await bot.send_group_msg(group_id=event.group_id, message="禁用成功")
        file = open("data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if event.group_id in file_dict["data"]:
            raise IgnoredException("该群未启用此节点")
    if not sudo:
        file = open("data/blacklist.json", "r")
        file_data = file.read()
        file.close()
        blacklist = json.loads(file_data)
        if event.get_user_id() in blacklist["data"]:
            raise IgnoredException("该用户被禁用")
