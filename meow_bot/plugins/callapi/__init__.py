import json
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, Message
from nonebot.plugins import PluginMetadata
from nonebot.permission import SUPERUSER

__plugin_meta__ = PluginMetadata(
    name="调用API",
    description="调用go-cqhttp API",
    usage="(权限: 超级用户)[命令前缀]callapi [API名称] [API参数(JSON)]: 调用go-cqhttp API",
)

callapi = on_command("callapi", permission=SUPERUSER, block=True, priority=2)


@callapi.handle()
async def _(bot: Bot, msg: Message = CommandArg()):
    args = str(msg).split(" ")
    res = str(await bot.call_api(api=args[0], **json.loads(" ".join(args[1:]))))
    await callapi.finish(res)
