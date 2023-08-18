import random
from nonebot import on_message
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

reply = on_message(priority=1, block=False)


@reply.handle()
async def _(bot: Bot, event: MessageEvent,msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    if "我是傻逼" in content:
        await reply.finish("傻逼")
    elif "好骂" in content or "怼" in content or "被骂了" in content:
        await reply.finish("在这纷繁世界的漩涡里，\n有人愚昧无知，纵情嘲弄与咒骂。\n然而，我心灵深处有一片宁静，\n智慧和温和的回应，将迎难而上。\n以宽容和理性驱散争吵的浮云，\n不为无礼之辞所玷污内心平衡。\n你言语刺伤，我用心灵反击，\n展现智慧与从容的力量，不卑不亢。\n对待挑衅，要有智者的姿态，\n坚守底线，不为情绪所驱使。\n让沉静的思考和理性的话语，\n逐渐化解争端，重建彼此的尊严。\n我们不为短暂的争斗而动心，\n宽容与智慧将引领我们前行。\n愿你也能明白，谩骂不能埋没真相，\n团结与理解，才是彼此成长的良方。")