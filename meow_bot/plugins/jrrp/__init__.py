from datetime import date, datetime, timezone, timedelta
import random
from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

__plugin_meta__ = PluginMetadata(
    name="jrrp",
    description="获取今日人品",
    usage="发送 [命令前缀]jrrp",
)

CST = timezone(timedelta(hours=8))

jrrp = on_command("jrrp", block=True, priority=2)

@jrrp.handle()
async def _(bot: Bot, event: MessageEvent):
    today = datetime.now(CST)
    if today.date() == date(2026, 9, 19):
        await jrrp.finish(f"你今天的人品是：100", at_sender=True, reply_message=True)
    rng = random.Random(f"{event.get_user_id()}{today.strftime('%Y%m%d')}")
    await jrrp.finish(f"你今天的人品是：{rng.randint(0, 100)}", at_sender=True, reply_message=True)