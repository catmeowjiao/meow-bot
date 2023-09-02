import nonebot
import time
import os
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.permission import SUPERUSER

update = on_command("update", permission=SUPERUSER, block=True, priority=2)


@update.handle()
async def _(bot: Bot):
    await update.send("正在更新")
    os.system("python3 update.py")
    await update.send("更新完成")
    file = open("data/reboot.py", "w")
    file.write(str(time.time()))
    file.close()
