import nonebot
import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Bot,
    Message,
    MessageEvent,
    GroupMessageEvent,
    PrivateMessageEvent,
)
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

switchmain = on_command("sm", permission=SUPERUSER, block=True, priority=2)
switchdevelop = on_command("sd", permission=SUPERUSER, block=True, priority=2)
enableall = on_command("ea", permission=SUPERUSER, block=True, priority=2)
disableall = on_command("da", permission=SUPERUSER, block=True, priority=2)
switchmainall = on_command("sma", permission=SUPERUSER, block=True, priority=2)
switchdevelopall = on_command("sda", permission=SUPERUSER, block=True, priority=2)
enableallall = on_command("eaa", permission=SUPERUSER, block=True, priority=2)
disableallall = on_command("daa", permission=SUPERUSER, block=True, priority=2)


@switchmain.handle()
async def _(bot: Bot, event: MessageEvent, msg: Message = CommandArg()):
    group_id = int(msg.extract_plain_text())
    file = open("../meow-bot/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id not in file_dict["data"]:
        file_dict["data"].append(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot/data/node.json", "w")
    file.write(file_data)
    file.close()
    file = open("../meow-bot-2/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id in file_dict["data"]:
        file_dict["data"].remove(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot-2/data/node.json", "w")
    file.write(file_data)
    file.close()
    await switchmain.finish("切换成功")


@switchdevelop.handle()
async def _(bot: Bot, event: MessageEvent, msg: Message = CommandArg()):
    group_id = int(msg.extract_plain_text())
    file = open("../meow-bot/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id in file_dict["data"]:
        file_dict["data"].remove(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot/data/node.json", "w")
    file.write(file_data)
    file.close()
    file = open("../meow-bot-2/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id not in file_dict["data"]:
        file_dict["data"].append(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot-2/data/node.json", "w")
    file.write(file_data)
    file.close()
    await switchdevelop.finish("切换成功")


@enableall.handle()
async def _(bot: Bot, event: MessageEvent, msg: Message = CommandArg()):
    group_id = int(msg.extract_plain_text())
    file = open("../meow-bot/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id not in file_dict["data"]:
        file_dict["data"].append(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot/data/node.json", "w")
    file.write(file_data)
    file.close()
    file = open("../meow-bot-2/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id not in file_dict["data"]:
        file_dict["data"].append(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot-2/data/node.json", "w")
    file.write(file_data)
    file.close()
    await enableall.finish("启用成功")


@disableall.handle()
async def _(bot: Bot, event: MessageEvent, msg: Message = CommandArg()):
    group_id = int(msg.extract_plain_text())
    file = open("../meow-bot/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id in file_dict["data"]:
        file_dict["data"].remove(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot/data/node.json", "w")
    file.write(file_data)
    file.close()
    file = open("../meow-bot-2/data/node.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if group_id in file_dict["data"]:
        file_dict["data"].remove(group_id)
    file_data = json.dumps(file_dict)
    file = open("../meow-bot-2/data/node.json", "w")
    file.write(file_data)
    file.close()
    await disableall.finish("禁用成功")


@switchmainall.handle()
async def _(bot: Bot, event: MessageEvent):
    group_list = await bot.get_group_list()
    for group in group_list:
        group_id = group["group_id"]
        file = open("../meow-bot/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id not in file_dict["data"]:
            file_dict["data"].append(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot/data/node.json", "w")
        file.write(file_data)
        file.close()
        file = open("../meow-bot-2/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id in file_dict["data"]:
            file_dict["data"].remove(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot-2/data/node.json", "w")
        file.write(file_data)
        file.close()
    await switchmainall.finish("切换成功")


@switchdevelopall.handle()
async def _(bot: Bot, event: MessageEvent):
    group_list = await bot.get_group_list()
    for group in group_list:
        group_id = group["group_id"]
        file = open("../meow-bot/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id in file_dict["data"]:
            file_dict["data"].remove(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot/data/node.json", "w")
        file.write(file_data)
        file.close()
        file = open("../meow-bot-2/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id not in file_dict["data"]:
            file_dict["data"].append(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot-2/data/node.json", "w")
        file.write(file_data)
        file.close()
    await switchdevelopall.finish("切换成功")


@enableallall.handle()
async def _(bot: Bot, event: MessageEvent):
    group_list = await bot.get_group_list()
    for group in group_list:
        group_id = group["group_id"]
        file = open("../meow-bot/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id not in file_dict["data"]:
            file_dict["data"].append(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot/data/node.json", "w")
        file.write(file_data)
        file.close()
        file = open("../meow-bot-2/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id not in file_dict["data"]:
            file_dict["data"].append(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot-2/data/node.json", "w")
        file.write(file_data)
        file.close()
    await enableallall.finish("启用成功")


@disableallall.handle()
async def _(bot: Bot, event: MessageEvent):
    group_list = await bot.get_group_list()
    for group in group_list:
        group_id = group["group_id"]
        file = open("../meow-bot/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id in file_dict["data"]:
            file_dict["data"].remove(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot/data/node.json", "w")
        file.write(file_data)
        file.close()
        file = open("../meow-bot-2/data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if group_id in file_dict["data"]:
            file_dict["data"].remove(group_id)
        file_data = json.dumps(file_dict)
        file = open("../meow-bot-2/data/node.json", "w")
        file.write(file_data)
        file.close()
    await disableallall.finish("禁用成功")
