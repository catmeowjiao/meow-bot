from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
    MessageEvent,
)
from nonebot.adapters.onebot.v11.event import Sender
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="sudo",
    description="以其他用户的身份请求指令",
    usage="发送 [命令前缀]sudo <QQ号> <指令>，例如：/sudo 1234567 /jrrp",
)

sudo = on_command("sudo", permission=SUPERUSER, priority=1, block=True)


@sudo.handle()
async def handle_sudo(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    try:
        user_id_text, command_text = str(args).strip().split(maxsplit=1)
        user_id = int(user_id_text)
        if user_id <= 0 or not command_text.strip():
            raise ValueError
    except ValueError:
        await sudo.finish("用法：/sudo <QQ号> <指令>\n例如：/sudo 1234567 /jrrp")

    if isinstance(event, GroupMessageEvent):
        try:
            member_info = await bot.call_api(
                "get_group_member_info",
                group_id=event.group_id,
                user_id=user_id,
                no_cache=True,
            )
            sender = Sender.model_validate(member_info)
        except Exception:
            await sudo.finish(f"无法获取群成员 {user_id} 的信息，请确认该用户在本群中")
    else:
        sender = Sender(user_id=user_id)

    message = Message(command_text)
    sudo_event = event.model_copy(
        update={
            "user_id": user_id,
            "message": message.copy(),
            "original_message": message.copy(),
            "raw_message": str(message),
            "sender": sender,
            "to_me": False,
            "reply": None,
        }
    )
    await bot.handle_event(sudo_event)
