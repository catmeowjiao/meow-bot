from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import MessageEvent, Message, Bot, GroupMessageEvent
from .run import run

runcode = on_command("code", block=True, priority=2)


@runcode.handle()
async def runcode_body(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    code = str(arg).strip()
    res = await run(code)
    messages = {
        "type": "node",
        "data": {"name": "return", "uin": bot.self_id, "content": Message(res)},
    }
    if isinstance(event, GroupMessageEvent):
        return await bot.call_api(
            "send_group_forward_msg", group_id=event.group_id, messages=messages
        )
    else:
        return await bot.call_api(
            "send_private_forward_msg", user_id=event.user_id, messages=messages
        )
