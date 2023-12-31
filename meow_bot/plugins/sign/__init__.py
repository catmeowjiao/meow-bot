import nonebot
import time
import random
import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(name="test", description="test", usage="test")
sign = on_command("sign", block=True, priority=2)


@sign.handle()
async def _(bot: Bot, event: MessageEvent):
    file = open("data/sign.json", "r")
    file_data = file.read()
    file.close()
    file_dict = json.loads(file_data)
    if event.get_user_id() in file_dict.keys() and file_dict[
        event.get_user_id()
    ] == int((time.time() + 28800) / 86400):
        await sign.finish("您今天已经签到过了")
    file_dict[event.get_user_id()] = int((time.time() + 28800) / 86400)
    file_data = json.dumps(file_dict)
    file = open("data/sign.json", "w")
    file.write(file_data)
    file.close()
    if event.get_user_id() == "3493487882":
        await sign.finish("签到成功! 您有无限卡, 因此不发放点数")
    file1 = open("data/chatgpt.json")
    file1_data = file1.read()
    file1.close()
    file1_dict = json.loads(file1_data)
    if event.get_user_id() not in file1_dict.keys():
        file1_dict[event.get_user_id()] = 1000
    file2 = open("data/gpt4.json")
    file2_data = file2.read()
    file2.close()
    file2_dict = json.loads(file2_data)
    if event.get_user_id() not in file2_dict.keys():
        file2_dict[event.get_user_id()] = 1000
    points = random.randint(500, 700)
    points2 = random.randint(100, 300)
    file1_dict[event.get_user_id()] += points
    file2_dict[event.get_user_id()] += points2
    cur = file1_dict[event.get_user_id()]
    cur2 = file2_dict[event.get_user_id()]
    file1_data = json.dumps(file1_dict)
    file1 = open("data/chatgpt.json", "w")
    file1.write(file1_data)
    file1.close()
    file2_data = json.dumps(file2_dict)
    file2 = open("data/gpt4.json", "w")
    file2.write(file2_data)
    file2.close()
    await sign.finish(
        "签到成功! 您获得了"
        + str(points)
        + "普通点数, "
        + str(points2)
        + "GPT4点数, 您的剩余普通点数为: "
        + str(cur)
        + ", 您的剩余GPT4点数为: "
        + str(cur2)
    )
