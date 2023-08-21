import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Message, MessageEvent, GroupMessageEvent
from nonebot.message import event_preprocessor
from nonebot.exception import IgnoredException
from nonebot.permission import SUPERUSER

switchmain = on_command("sm", permission=SUPERUSER, priority=2, block=True)
switchdevelop = on_command("sd", permission=SUPERUSER, priority=2, block=True)
enableall = on_command("ea", permission=SUPERUSER, priority=2, block=True)


@event_preprocessor
async def _(event: GroupMessageEvent):
    file = open("data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if event.group_id in file_dict["data"]:
        raise IgnoredException("该群未启用此节点")


@switchmain.handle()
async def _(bot: Bot, event: GroupMessageEvent):
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


@switchdevelop.handle()
async def _(bot: Bot, event: GroupMessageEvent):
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


@enableall.handle()
async def _(bot: Bot, event: GroupMessageEvent):
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
