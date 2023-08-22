import nonebot
import psutil
import time
import sys
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

status = on_command("status", block=True, priority=2)

runtime = time.time()


@driver.on_startup
async def _():
    global runtime
    runtime = time.time()


@status.handle()
async def _(bot: Bot, event: MessageEvent):
    await status.finish(
        f"CPU占用: {psutil.cpu_percent()}%\n内存使用量: {psutil.virtual_memory().percent}%\n运行时间: {time.time() - runtime}秒\n系统类型: {sys.platform}"
    )
