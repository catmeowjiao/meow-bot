import time
import random
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent

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
        await reply.finish("傻逼")
    elif content == "6":
        if event.group_id not in sixcache.keys():
            sixcache[event.group_id] = 0
        if time.time() - sixcache[event.group_id] > 7:
            sixcache[event.group_id] = time.time()
            await reply.finish("六真言? 6!")
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
        await reply.finish(
            "六字真言? 在我这里管用! 虽然但是\n在这纷繁世界的漩涡里，\n有人愚昧无知，纵情嘲弄与咒骂。\n然而，我心灵深处有一片宁静，\n智慧和温和的回应，将迎难而上。\n\n以宽容和理性驱散争吵的浮云，\n不为无礼之辞所玷污内心平衡。\n你言语刺伤，我用心灵反击，\n展现智慧与从容的力量，不卑不亢。\n\n对待挑衅，要有智者的姿态，\n坚守底线，不为情绪所驱使。\n让沉静的思考和理性的话语，\n逐渐化解争端，重建彼此的尊严。\n\n我们不为短暂的争斗而动心，\n宽容与智慧将引领我们前行。\n愿你也能明白，谩骂不能埋没真相，\n团结与理解，才是彼此成长的良方。\n\n所以, 典!"
        )
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
            await bot.call_api(
                "send_group_msg", group_id=event.group_id, message=content
            )
        else:
            lastcache[event.group_id] = {"content": content, "time": time.time()}
