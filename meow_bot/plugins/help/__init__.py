import nonebot
import random
from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    GroupMessageEvent,
    PrivateMessageEvent,
)

help = on_command("help", aliases={"menu"}, block=True, priority=2)


@help.handle()
async def _(bot: Bot, event: MessageEvent):
    if event.get_user_id() == "3493487882":
        await help.send("你好, meowjiao!")
    messages = [
        {
            "type": "node",
            "data": {
                "uin": event.self_id,
                "name": f"MeowBot Help Menu",
                "content": 'MeowBot Help Menu\nhelp: 获取帮助\n(必须@Bot) 命令前缀 + 问题: 向ChatGPT提问(不保留历史消息)\nchat + 问题: 向ChatGPT提问(保留历史消息)\nreset + 提示词: 重置历史记录并设置提示词(若不填提示词则设置为普通模式)\nreset_dev: 重置历史记录并设置为开发者模式\nquery: 查询剩余MeowBot ChatGPT点数\n(超级用户专用) change + 被更改点数的用户的QQ号 + 空格 + 目标点数: 改变用户MeowBot ChatGPT点数\n(超级用户专用) buy + 被充值用户的QQ号 + 空格 + 充值点数: 为该用户充值\npay + 被转账用户的QQ号 + 空格 + 转账点数: 将自己的点数转账给该用户\nstatus: 获取服务器状态\ncode + 语言 + 换行 + 代码: 运行程序(无输入)\ncode + 语言 + 空格 + 输入 + 换行 + 代码: 运行程序(有输入)\n(超级用户专用) reboot: 重启Bot\n(超级用户专用) poweroff: 关闭Bot\n(超级用户专用) manager: 插件管理器\n(超级用户专用) callapi: 调用go-cqhttp API\n(超级用户专用) atall: Bot分别@群里的每一位成员\npreview + 网站链接(需带请求头): 获取网站预览图片\njrrp: 获取今日人品\nsign: 签到, 会获得500 ~ 700之间的随机点数, 点数可用于MeowBot ChatGPT\n(超级用户专用) update: 更新Bot, 有可能因为无法访问Github而卡住\n(超级用户专用) sudo + QQ号 + 空格 + 指令: 以他人身份运行指令\nticket: 花费100点数购买一张彩票, 彩票开出的点数随机, 下限为0, 上限为500 ~ 1000中的随机整数.\n(超级用户专用) ban + 要封禁的QQ号: 解除该用户的Bot使用权\n(超级用户专用) unban + 要解除封禁的QQ号: 授予该用户Bot使用权\nblacklist: 列出封禁用户列表\n(超级用户专用) bc + 要发送的消息: 往Bot加入的所有群内都发送这条消息\n(超级用户专用) bcl + 要禁用的群号: 该群禁用超管广播\n(超级用户专用) bcul + 要启用的群号: 该群启用超管广播\n消息中的左括号没有对应的右括号: Bot自动回复缺少的右括号("([)]"不被认为是匹配的括号, 因此Bot不会补全"([)"这种)\n一号节点(main节点)命令前缀: "/", "%"\n二号节点(develop节点)命令前缀: ".", "!"\nCopyright 2023 meowjiao',
            },
        }
    ]
    if isinstance(event, GroupMessageEvent):
        await bot.call_api(
            "send_group_forward_msg", group_id=event.group_id, messages=messages
        )
    else:
        await bot.call_api(
            "send_private_forward_msg", user_id=event.user_id, messages=messages
        )
