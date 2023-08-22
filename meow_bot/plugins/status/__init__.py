import nonebot
import psutil
import time
import sys
from nonebot import on_command, get_driver
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

driver = get_driver()
runtime = time.time()

status = on_command("status", block=True, priority=2)


@driver.on_startup
async def _():
    global runtime
    runtime = time.time()


@status.handle()
async def _(bot: Bot, event: MessageEvent):
    await status.finish(
        f"CPU占用: {psutil.cpu_percent()}%\n内存使用量: {psutil.virtual_memory().percent}%\n运行时间: {time.time() - runtime}秒\n系统类型: {sys.platform}"
    )
