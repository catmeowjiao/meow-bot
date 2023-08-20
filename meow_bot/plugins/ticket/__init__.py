import nonebot
import json
import random
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Message, MessageEvent

buy_ticket = on_command("ticketbuy", block=True, priority=2)


@buy_ticket.handle()
async def _(event: MessageEvent, msg: Message = CommandArg()):
    if event.get_user_id() == "3493487882":
        await buy_ticket.send("购买成功! 本次购买不消耗点数, 正在开奖...")
        res = random.randint(0, random.randint(500, 1000))
        await buy_ticket.finish(f"您开出了{res}点, 您有无限卡, 因此不发放点数")
    file = open("data/chatgpt.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if event.get_user_id() not in file_dict.keys():
        file_dict[event.get_user_id()] = 1000
    if file_dict[event.get_user_id()] < 100:
        await buy_ticket.finish("点数不足!")
    file_dict[event.get_user_id()] -= 100
    await buy_ticket.send("购买成功! 本次消耗100点数, 正在开奖...")
    res = random.randint(0, random.randint(500, 1000))
    file_dict[event.get_user_id()] += res
    await buy_ticket.finish(
        f"您开出了{res}点, 您的剩余点数为: {file_dict[event.get_user_id()]}点"
    )
    file_data = json.dumps(file_dict)
    file = open("data/chatgpt.json", "w")
    file.write(file_data)
    file.close()
