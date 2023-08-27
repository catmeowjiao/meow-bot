import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Message, MessageEvent
from nonebot.exception import IgnoredException
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

broadcast = on_command("bc", permission=SUPERUSER, priority=2, block=True)
broadcastlock = on_command("bcl", permission=SUPERUSER, priority=2, block=True)
broadcastunlock = on_command("bcul", permission=SUPERUSER, priority=2, block=True)
broadcastlockview = on_command("bclv", priority=2, block=True)
broadcastuser = on_command("ubc", permission=SUPERUSER, priority=2, block=True)
broadcastlockuser = on_command("ubcl", permission=SUPERUSER, priority=2, block=True)
broadcastunlockuser = on_command("ubcul", permission=SUPERUSER, priority=2, block=True)
broadcastlockviewuser = on_command("ubclv", priority=2, block=True)


@broadcast.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    file = open("data/broadcast.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    group_list = await bot.get_group_list()
    for group in group_list:
        print(group["group_id"])
        if group["group_id"] not in file_dict["data"]:
            await bot.send_group_msg(
                group_id=group["group_id"], message="[超管广播] " + msg
            )
    await broadcast.finish("发送成功!")


@broadcastlock.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    id = int(arg.extract_plain_text().strip())
    file = open("data/broadcast.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if id not in file_dict["data"]:
        file_dict["data"].append(id)
    file_data = json.dumps(file_dict)
    file = open("data/broadcast.json", "w")
    file.write(file_data)
    await broadcastlock.finish("禁用成功!")


@broadcastunlock.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    id = int(arg.extract_plain_text().strip())
    file = open("data/broadcast.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if id in file_dict["data"]:
        file_dict["data"].remove(id)
    file_data = json.dumps(file_dict)
    file = open("data/broadcast.json", "w")
    file.write(file_data)
    await broadcastunlock.finish("启用成功!")


@broadcastlockview.handle()
async def _(bot: Bot, event: MessageEvent):
    file = open("data/broadcast.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    await broadcast.finish(str(file_dict["data"]))


@broadcastuser.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    file = open("data/broadcastuser.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    user_list = await bot.get_friend_list()
    for user in user_list:
        if user["user_id"] not in file_dict["data"]:
            await bot.send_private_msg(user_id=user["user_id"], message="[超管广播] " + msg)
    await broadcast.finish("发送成功!")


@broadcastlockuser.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    id = int(arg.extract_plain_text().strip())
    file = open("data/broadcastuser.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if id not in file_dict["data"]:
        file_dict["data"].append(id)
    file_data = json.dumps(file_dict)
    file = open("data/broadcastuser.json", "w")
    file.write(file_data)
    await broadcastlock.finish("禁用成功!")


@broadcastunlockuser.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    id = int(arg.extract_plain_text().strip())
    file = open("data/broadcastuser.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if id in file_dict["data"]:
        file_dict["data"].remove(id)
    file_data = json.dumps(file_dict)
    file = open("data/broadcastuser.json", "w")
    file.write(file_data)
    await broadcastunlock.finish("启用成功!")


@broadcastlockviewuser.handle()
async def _(bot: Bot, event: MessageEvent):
    file = open("data/broadcastuser.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    await broadcast.finish(str(file_dict["data"]))
