import json
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters import Bot
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message

file = open("data/blacklist.json", "r")
file_data = file.read()
file.close()
blacklist = json.loads(file_data)
ban = on_command("ban", permission=SUPERUSER, priority=2, block=True)
unban = on_command("unban", permission=SUPERUSER, priority=2, block=True)


@event_preprocessor
async def _(event: MessageEvent):
    if event.get_user_id() in blacklist["data"]:
        raise IgnoredException("该用户被禁用")


@ban.handle()
async def _(msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    if content == "3493487882":
        await ban.finish("超管不可封禁")
    if content not in blacklist["data"]:
        blacklist["data"].append(content)
    file = open("data/blacklist.json", "w")
    file_data = json.dumps(blacklist)
    file.write(file_data)
    file.close()
    await ban.finish("封禁成功!")


@unban.handle()
async def _(msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    if content == "3493487882":
        await unban.finish("超管无需解除封禁")
    if content in blacklist["data"]:
        blacklist["data"].remove(content)
    file = open("data/blacklist.json", "w")
    file_data = json.dumps(blacklist)
    file.write(file_data)
    file.close()
    await unban.finish("解除封禁成功!")
