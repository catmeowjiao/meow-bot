import nonebot
import random
import time
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(name="test", description="test", usage="test")
jrrp = on_command("jrrp", block=True, priority=2)


@jrrp.handle()
async def _(bot: Bot, event: MessageEvent):
    random.seed(
        int(event.get_user_id()) + int((time.time() + 28800) / 86400) * 2 + 114514
    )
    await jrrp.finish(f"你今天的人品是: {random.randint(0, 100)}")
