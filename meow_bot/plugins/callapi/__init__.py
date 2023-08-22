import nonebot
import json
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, Message
from nonebot.permission import SUPERUSER

callapi = on_command("callapi", permission=SUPERUSER, block=True, priority=2)


@callapi.handle()
async def _(bot: Bot, msg: Message = CommandArg()):
    args = str(msg).split(" ")
    res = str(await bot.call_api(api=args[0], **json.loads(" ".join(args[1:]))))
    await callapi.finish(res)
