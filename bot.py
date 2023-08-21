import nonebot
import os
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

if not os.path.isdir("data"):
    os.mkdir("data")

if not os.path.isfile("data/chatgpt.json"):
    file = open("data/chatgpt.json", "w")
    file.write("{}")
    file.close()

if not os.path.isfile("data/sign.json"):
    file = open("data/sign.json", "w")
    file.write("{}")
    file.close()

if not os.path.isfile("data/broadcast.json"):
    file = open("data/broadcast.json", "w")
    file.write('{"data":[]}')
    file.close()

if not os.path.isfile("data/broadcastuser.json"):
    file = open("data/broadcastuser.json", "w")
    file.write('{"data":[]}')
    file.close()

if not os.path.isfile("data/blacklist.json"):
    file = open("data/blacklist.json", "w")
    file.write('{"data":[]}')
    file.close()

if not os.path.isfile("data/node.json"):
    file = open("data/node.json", "w")
    file.write("{}")
    file.close()

nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()
