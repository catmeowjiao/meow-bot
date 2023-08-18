import random
from nonebot import on_message
from nonebot.params import EventPlainText
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

reply_list = ["SB","L","LLL","打字慢","亲手sudo rm -rf /*"]

reply = on_message(priority=1, block=False)


@reply.handle()
async def _(bot: Bot, event: MessageEvent):
    if event.get_user_id() == "3493487882":
        num = random.randint(0,9)
        if num >= 0 and num <= 2:
            res = random.choice(reply_list)
            await reply.finish(res)

