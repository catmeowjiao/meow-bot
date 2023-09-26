import time
import random
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="自动回复",
    description="自动回复",
    usage="本插件有关键字回复, 随机回复和跟风回复\n关键字回复请阅读代码或自行探索\n随机回复会发送MeowBot开源地址, 概率2%\n跟风回复会在10秒内连续发送两条消息且上次的7秒冷冻期已结束的情况下跟风回复",
)
reply = on_message(priority=1, block=False)
lastcache = {}
lastsendtime = {}
sixcache = {}


@reply.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    global last
    global laststr
    content = str(event.get_message())
    if "我是傻逼" in content:
        await reply.finish("我才是傻逼!")
    elif content == "6":
        if event.group_id not in sixcache.keys():
            sixcache[event.group_id] = 0
        if time.time() - sixcache[event.group_id] > 7:
            sixcache[event.group_id] = time.time()
            await reply.finish("六真言? 6")
    elif (
        content == "典"
        or content == "孝"
        or content == "急"
        or content == "乐"
        or content == "蚌"
        or content == "批"
        or content == "赢"
        or content == "麻"
        or content == "盒"
        or content == "寄"
        or content == "创"
        or content == "绝"
        or content == "对"
        or "原神怎么你了" in content
    ):
        await reply.finish("六字真言? 乐")
    elif content == "114514":
        await reply.finish("114514")
    else:
        if event.group_id not in lastsendtime.keys():
            lastsendtime[event.group_id] = 0
        if (
            event.group_id in lastcache.keys()
            and content == lastcache[event.group_id]["content"]
            and time.time() - lastcache[event.group_id]["time"] <= 10
            and time.time() - lastsendtime[event.group_id] > 7
        ):
            del lastcache[event.group_id]
            lastsendtime[event.group_id] = time.time()
            await reply.finish(content)
        else:
            lastcache[event.group_id] = {"content": content, "time": time.time()}
            rand = random.randint(0, 50)
            if rand == 0:
                await reply.finish(
                    "MeowBot开源地址: https://github.com/catmeowjiao/meow-bot"
                )
