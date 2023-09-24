from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

__plugin_meta__ = PluginMetadata(
    name="@全体成员", description="Bot分别@每位群成员", usage="(权限: 超级用户)[命令前缀]atall: Bot分别@每位群成员"
)

atall = on_command("atall", permission=SUPERUSER, priority=2, block=True)


@atall.handle()
async def _(bot: Bot, event: MessageEvent):
    user_list = await bot.get_group_member_list(group_id=event.group_id)
    res = ""
    for user in user_list:
        res += f"[CQ:at,qq=" + str(user["user_id"]) + "]"
    await bot.send_group_msg(group_id=event.group_id, message=res)
