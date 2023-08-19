import json
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters import Bot
from nonebot.adapters.onebot.v11 import MessageEvent
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
    if event.get_user_id() in blacklistdata:
        raise IgnoredException("该用户被禁用")


@ban.handle()
async def _(msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    if content not in blacklist:
        blacklist.append(content)
    file = open("data/blacklist.json", "w")
    file_data = json.dumps(blacklist)
    file.write(file_data)
    file.close()
    await ban.send("封禁成功!")


@unban.handle()
async def _(msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    if content in blacklist:
        blacklist.remove(content)
    file = open("data/blacklist.json", "w")
    file_data = json.dumps(blacklist)
    file.write(file_data)
    file.close()
    await unban.send("取消封禁成功!")
