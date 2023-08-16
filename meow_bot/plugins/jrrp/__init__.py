import nonebot
import random
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

help = on_command("jrrp", block=True, priority=2)


@help.handle()
async def _(bot: Bot, event: MessageEvent):
    await help.finish(f"你今天的人品是: {random.randint(0, 100)}")
