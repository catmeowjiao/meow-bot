import asyncio
import json
from argparse import Namespace
from nonebot.matcher import Matcher
from nonebot.params import ShellCommandArgs
from nonebot.message import run_preprocessor, event_preprocessor, event_postprocessor
from nonebot.exception import IgnoredException, ActionFailed
from nonebot.plugin import on_shell_command, get_loaded_plugins
from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    Message,
    MessageEvent,
    GroupMessageEvent,
)
from nonebot.permission import SUPERUSER
from nonebot import get_driver
from .handle import Handle
from .parser import npm_parser
from .manager import plugin_manager
from .config import Config

config = Config.parse_obj(get_driver().config)
npm = on_shell_command("manager", parser=npm_parser, priority=2, block=True)

_sudo_original_user: dict[int, MessageEvent] = {}


@event_postprocessor
async def sudo_postprocessor(event: MessageEvent):
    if not hasattr(event, "_sudo_original_user"):
        return
    if event.user_id in _sudo_original_user.keys():
        _sudo_original_user.pop(event.user_id)


@event_preprocessor
async def sudo_command(event: MessageEvent, bot: Bot):
    for command_start in get_driver().config.command_start:
        if event.raw_message.startswith(
            f"{command_start}sudo"
        ) and event.get_user_id() in list(config.sudoers):
            event._sudo_original_user = event.user_id
            event.user_id = get_user_id(event)
            if event.message_type == "private":
                while event.user_id in _sudo_original_user.keys():
                    await asyncio.sleep(0.1)
                _sudo_original_user[event.user_id] = event
            if config.sudo_replace_sender_data:
                await change_sender_data(bot, event)
            cmd_start = command_start if config.sudo_insert_cmdstart else ""
            change_message(event, cmd_start)
            break


async def _(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        file = open("data/node.json", "r")
        file_data = file.read()
        file.close()
        file_dict = json.loads(file_data)
        if event.group_id not in file_dict["data"]:
            raise IgnoredException("该群未启用此节点")
    if not event.user_id in _sudo_original_user.keys():
        file = open("data/blacklist.json", "r")
        file_data = file.read()
        file.close()
        blacklist = json.loads(file_data)
        if event.get_user_id() in blacklist["data"]:
            raise IgnoredException("该用户被禁用")


async def change_sender_data(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        try:
            user_info = await bot.get_group_member_info(
                group_id=event.group_id,
                user_id=event.user_id,
                no_cache=True,
            )
            event.sender.age = user_info["age"]
            event.sender.level = user_info["level"]
            event.sender.sex = user_info["sex"]
            event.sender.nickname = user_info["nickname"]
            event.sender.area = user_info["area"]
            event.sender.card = user_info["card"]
            event.sender.role = user_info["role"]
        except ActionFailed:
            user_info = await bot.get_stranger_info(
                user_id=event.user_id, no_cache=True
            )
            event.sender.age = user_info["age"]
            event.sender.level = user_info["level"]
            event.sender.sex = user_info["sex"]
            event.sender.nickname = user_info["nickname"]
    else:
        user_info = await bot.get_stranger_info(user_id=event.user_id, no_cache=True)
        event.sender.age = user_info["age"]
        event.sender.level = user_info["level"]
        event.sender.sex = user_info["sex"]
        event.sender.nickname = user_info["nickname"]


def get_user_id(event: MessageEvent) -> int:
    message_start = event.message[0].data["text"]
    try:
        return message_start.strip().split(" ")[1]
    except IndexError:
        return event.message[1].data["qq"]


def change_message(event: MessageEvent, cmd_start) -> None:
    if tmp_message := " ".join(event.message[0].data["text"].split(" ")[2:]):
        event.message[0].data["text"] = cmd_start + tmp_message
    else:
        event.message.pop(0)
        event.message.pop(0)
        event.message[0].data["text"] = (
            cmd_start + event.message[0].data["text"].strip()
        )


@Bot.on_calling_api
async def handle_api_call(_bot: Bot, api: str, data: dict[str, any]):
    if (
        (api == "send_msg" and data["message_type"] == "private")
        or api in ["send_private_forward_msg", "send_private_msg"]
    ) and data["user_id"] in _sudo_original_user.keys():
        data["user_id"] = _sudo_original_user[data["user_id"]]._sudo_original_user


# 在 Matcher 运行前检测其是否启用
@run_preprocessor
async def _(matcher: Matcher, bot: Bot, event: Event):
    if not event.user_id in _sudo_original_user.keys():
        plugin = matcher.plugin_name

        conv = {
            "user": [event.user_id] if hasattr(event, "user_id") else [],  # type: ignore
            "group": [event.group_id] if hasattr(event, "group_id") else [],  # type: ignore
        }

        plugin_manager.update_plugin(
            {
                str(p.name): p.name != "nonebot_plugin_manager" and bool(p.matcher)
                for p in get_loaded_plugins()
            }
        )

        if plugin and not plugin_manager.get_plugin(conv=conv, perm=1)[plugin]:
            raise IgnoredException(f"Nonebot Plugin Manager has blocked {plugin} !")


@npm.handle()
async def _(bot: Bot, event: MessageEvent, args: Namespace = ShellCommandArgs()):
    args.conv = {
        "user": [event.user_id],
        "group": [event.group_id] if isinstance(event, GroupMessageEvent) else [],
    }
    args.is_admin = (
        event.sender.role in ["admin", "owner"]
        if isinstance(event, GroupMessageEvent)
        else False
    )
    args.is_superuser = str(event.user_id) in bot.config.superusers

    if hasattr(args, "handle"):
        message = getattr(Handle, args.handle)(args)
        if message is not None:
            message = message.split("\n")
            if len(message) > 15:
                i = 1
                messages = []
                while len(message) > 15:
                    messages.append("\n".join(message[:15]) + f"\n【第{i}页】")
                    message = message[15:]
                    i = i + 1
                messages.append("\n".join(message[:15]) + f"\n【第{i}页-完】")
                if isinstance(event, GroupMessageEvent):
                    await bot.send_group_forward_msg(
                        group_id=event.group_id,
                        messages=[
                            {
                                "type": "node",
                                "data": {
                                    "name": "NBPM",
                                    "uin": bot.self_id,
                                    "content": msg,
                                },
                            }
                            for msg in messages
                        ],
                    )
                else:
                    await bot.send_private_forward_msg(
                        user_id=event.user_id,
                        messages=[
                            {
                                "type": "node",
                                "data": {
                                    "name": "NBPM",
                                    "uin": bot.self_id,
                                    "content": msg,
                                },
                            }
                            for msg in messages
                        ],
                    )
            else:
                await bot.send(event, "\n".join(message[:30]))
