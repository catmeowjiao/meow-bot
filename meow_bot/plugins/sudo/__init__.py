from contextvars import ContextVar
from typing import Any

from nonebot import on_command
from nonebot.adapters import Bot as BaseBot
from nonebot.adapters.onebot.v11 import (
    Bot as OneBotBot,
    GroupMessageEvent,
    Message,
    MessageEvent,
)
from nonebot.adapters.onebot.v11.event import Sender
from nonebot.adapters.onebot.v11.exception import OneBotV11AdapterException
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="sudo",
    description="以其他用户的身份请求指令",
    usage="发送 [命令前缀]sudo <QQ号> <指令>，例如：/sudo 1234567 /jrrp",
)

sudo = on_command("sudo", permission=SUPERUSER, priority=1, block=True)

_sudo_context: ContextVar[tuple[str, int, int] | None] = ContextVar(
    "sudo_context", default=None
)
_private_message_apis = {"send_private_msg", "send_private_forward_msg"}


def is_sudo_command(bot: OneBotBot, message: str) -> bool:
    command = message.lstrip().split(maxsplit=1)[0]
    return any(command == f"{prefix}sudo" for prefix in bot.config.command_start)


async def get_stranger_sender(
    bot: OneBotBot, user_id: int, *, in_group: bool
) -> Sender:
    try:
        user_info = await bot.call_api(
            "get_stranger_info", user_id=user_id, no_cache=True
        )
        sender = Sender.model_validate(user_info).model_copy(update={"user_id": user_id})
    except OneBotV11AdapterException:
        sender = Sender(user_id=user_id)

    if in_group:
        sender = sender.model_copy(update={"role": "member"})
    return sender


async def get_sender(bot: OneBotBot, event: MessageEvent, user_id: int) -> Sender:
    if not isinstance(event, GroupMessageEvent):
        return await get_stranger_sender(bot, user_id, in_group=False)

    try:
        member_info = await bot.call_api(
            "get_group_member_info",
            group_id=event.group_id,
            user_id=user_id,
            no_cache=True,
        )
        return Sender.model_validate(member_info).model_copy(update={"user_id": user_id})
    except OneBotV11AdapterException:
        return await get_stranger_sender(bot, user_id, in_group=True)


def redirect_at_sender(message: Message, sudo_user_id: int, caller_user_id: int) -> None:
    at_index = 1 if message and message[0].type == "reply" else 0
    if len(message) <= at_index:
        return

    segment = message[at_index]
    if segment.type == "at" and str(segment.data.get("qq")) == str(sudo_user_id):
        segment.data["qq"] = str(caller_user_id)


@BaseBot.on_calling_api
async def redirect_sudo_result(
    bot: BaseBot, api: str, data: dict[str, Any]
) -> None:
    if not isinstance(bot, OneBotBot):
        return

    context = _sudo_context.get()
    if context is None:
        return

    self_id, sudo_user_id, caller_user_id = context
    if str(bot.self_id) != self_id or str(data.get("user_id")) != str(sudo_user_id):
        return

    is_private_message = api in _private_message_apis or (
        api == "send_msg"
        and data.get("message_type") in (None, "private")
        and data.get("group_id") is None
    )
    if is_private_message:
        data["user_id"] = caller_user_id
        return

    if data.get("group_id") is None or "message" not in data:
        return

    message = data["message"]
    if not isinstance(message, Message):
        message = Message(message)
        data["message"] = message
    redirect_at_sender(message, sudo_user_id, caller_user_id)


@sudo.handle()
async def handle_sudo(
    bot: OneBotBot, event: MessageEvent, args: Message = CommandArg()
) -> None:
    try:
        user_id_text, command_text = str(args).strip().split(maxsplit=1)
        if not user_id_text.isascii() or not user_id_text.isdecimal():
            raise ValueError
        user_id = int(user_id_text)
        if user_id <= 0 or not command_text.strip():
            raise ValueError
    except ValueError:
        await sudo.finish("用法：/sudo <QQ号> <指令>\n例如：/sudo 1234567 /jrrp")

    if is_sudo_command(bot, command_text):
        await sudo.finish("不允许嵌套使用 sudo")

    await sudo.send(f"正在以 {user_id} 的身份运行指令")

    sender = await get_sender(bot, event, user_id)
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

    token = _sudo_context.set((str(bot.self_id), user_id, event.user_id))
    try:
        await bot.handle_event(sudo_event)
    finally:
        _sudo_context.reset(token)
