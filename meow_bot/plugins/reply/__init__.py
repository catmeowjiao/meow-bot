import time
import random
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent

reply = on_message(priority=1, block=False)
lastcache = {}


@reply.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    global last
    global laststr
    content = str(event.get_message())
    if "我是傻逼" in content:
        await reply.finish("傻逼")
    elif content == "6" and time.time() - sixlast > 10:
        sixlast = time.time()
        await reply.finish("6")
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
        num = random.randint(0, 1)
        if num == 0:
            await reply.finish("六字真言?在我这里不管用!")
    else:
        if (
            event.get_group_id() in lastcache.keys()
            and content == lastcache[event.get_group_id()]["content"]
            and time.time() - lastcache[event.get_group_id()]["time"] <= 10
        ):
            lastcache[event.get_group_id()] = {"content": content, "time": time.time()}
            await reply.finish(content)
        else:
            lastcache[event.get_group_id()] = {"content": content, "time": time.time()}
