from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

broadcast = on_command("bc", permission=SUPERUSER, priority=2, block=True)


@broadcast.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    if not msg:
        await broadcast.finish("请在指令后输入需要广播的消息")
    group_list = await bot.get_group_list()
    for group in group_list:
        await bot.send_group_msg(group_id=group["group_id"], message="[超管广播] " + msg)
    await broadcast.finish("发送成功!")
