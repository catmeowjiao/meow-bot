import nonebot
import time
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(name="test", description="test", usage="test")
reboot = on_command(
    "reboot", permission=SUPERUSER, aliases={"restart"}, block=True, priority=2
)


@reboot.handle()
async def _(bot: Bot):
    await reboot.send("已发送重启指令")
    file = open("data/reboot.py", "w")
    file.write(str(time.time()))
    file.close()
