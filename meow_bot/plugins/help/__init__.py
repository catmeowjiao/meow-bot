from nonebot import on_command, get_driver
from nonebot.plugin import PluginMetadata, get_loaded_plugins, get_plugin
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.adapters import Event, Message

command_starts = list(get_driver().config.command_start)
__plugin_meta__ = PluginMetadata(
    name="MeowBot Help Menu",
    description="MeowBot帮助菜单",
    usage=f"""[命令前缀]help: 获取help指令的帮助
[命令前缀]help list: 获取插件列表
[命令前缀]help [插件名]: 获取该插件帮助""",
)
help = on_command("help", priority=2, block=True)


@help.handle()
async def _(event: Event, args: Message = CommandArg()):
    if args:
        arg = args.extract_plain_text().strip()
        if arg == "list":
            plugins = get_loaded_plugins()
            plugin_names = []
            for plugin in plugins:
                plugin_names.append(f"{plugin.name} | {plugin.metadata.name}")
            plugin_names.sort()
            newline = "\n"
            await help.finish(f"{newline.join(plugin_names)}")
        else:
            plugin = get_plugin(arg)
            if not plugin:
                await help.finish(f"{arg}不存在")
            else:
                await help.finish(
                    f"""MeowBot Help Menu
命令前缀: {" ".join(command_starts)}
插件名称: {plugin.metadata.name}
插件描述: {plugin.metadata.description}
使用方法:
{plugin.metadata.usage}"""
                )
    else:
        await help.finish(
            f"""MeowBot Help Menu
命令前缀: {" ".join(command_starts)}
[命令前缀]help: 获取help指令的帮助
[命令前缀]help list: 获取插件列表
[命令前缀]help [插件名]: 获取该插件帮助"""
        )
