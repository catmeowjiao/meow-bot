import nonebot
import time
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.permission import SUPERUSER

poweroff = on_command(
    "reboot", permission=SUPERUSER, aliases={"restart"}, block=True, priority=2
)


@poweroff.handle()
async def _(bot: Bot):
    await poweroff.send("已发送重启指令")
    file = open("reboot.py", "w")
    file.write(str(time.time()))
    file.close()
