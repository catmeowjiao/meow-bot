import time
import random
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Message, MessageEvent

reply = on_message(priority=1, block=False)
sixlast = 0


@reply.handle()
async def _(bot: Bot, event: MessageEvent):
    global sixlast
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
    elif "好骂" in content or "怼" in content or "被骂了" in content:
        await reply.finish(
            "在这纷繁世界的漩涡里，\n有人愚昧无知，纵情嘲弄与咒骂。\n然而，我心灵深处有一片宁静，\n智慧和温和的回应，将迎难而上。\n以宽容和理性驱散争吵的浮云，\n不为无礼之辞所玷污内心平衡。\n你言语刺伤，我用心灵反击，\n展现智慧与从容的力量，不卑不亢。\n对待挑衅，要有智者的姿态，\n坚守底线，不为情绪所驱使。\n让沉静的思考和理性的话语，\n逐渐化解争端，重建彼此的尊严。\n我们不为短暂的争斗而动心，\n宽容与智慧将引领我们前行。\n愿你也能明白，谩骂不能埋没真相，\n团结与理解，才是彼此成长的良方。"
        )
