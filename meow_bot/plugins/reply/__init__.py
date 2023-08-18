from nonebot import on_message
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import Bot, MessageEvent


reply = on_message(check_brackets, priority=1, block=False)


@reply.handle()
async def _(bot: Bot, event: MessageEvent):
    if event.get_user_id() == "1951474558":
        await reply.finish("您好, 尊贵的SB用户")
