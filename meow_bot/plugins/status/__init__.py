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


def format_time(seconds):
    d = int(seconds / 86400)
    h = int(seconds / 3600) % 24
    m = int(seconds / 60) % 60
    s = int(seconds) % 60
    return f"{d}天{h}时{m}分{s}秒"


@status.handle()
async def _(bot: Bot, event: MessageEvent):
    await status.finish(
        f"CPU占用: {psutil.cpu_percent()}%\n内存使用量: {psutil.virtual_memory().percent}%\n运行时间: {format_time(time.time() - runtime)}\n系统类型: {sys.platform}"
    )
