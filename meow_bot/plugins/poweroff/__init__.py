import nonebot
import sys
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(name="test", description="test", usage="test")
poweroff = on_command(
    "poweroff", permission=SUPERUSER, aliases={"shutdown"}, block=True, priority=2
)


@poweroff.handle()
async def _(bot: Bot):
    await poweroff.send("已发送关机指令")
    sys.exit(0)
