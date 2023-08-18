from nonebot import on_message
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import Bot, MessageEvent


reply = on_message(priority=1, block=False)


@reply.handle()
async def _(bot: Bot, event: MessageEvent):
    if event.get_user_id() == "3493487882":
        await reply.finish("您好, SB")
