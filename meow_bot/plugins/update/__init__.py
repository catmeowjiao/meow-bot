import nonebot
import time
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.permission import SUPERUSER

update = on_command("update", permission=SUPERUSER, block=True, priority=2)


@update.handle()
async def _(bot: Bot):
    update.send("正在更新")
    os.system("git pull")
    update.send("更新完成, 正在重启")
    file = open("reboot.py", "w")
    file.write(str(time.time()))
    file.close()
