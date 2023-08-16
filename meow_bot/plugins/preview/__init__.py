import traceback
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment, MessageEvent
from nonebot.params import CommandArg
import os
from playwright.async_api import async_playwright
import time
import asyncio
import os.path

preview = on_command("preview", priority=2, block=True)


@preview.handle()
async def preview_website(event: MessageEvent, message: Message = CommandArg()):
    file_name = f"preview.image_{int(time.time())}"
    url = str(message)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await asyncio.sleep(1)
        url = page.url
        await page.screenshot(path=f"{file_name}.png", full_page=True)
        await browser.close()
    await preview.send(
        Message(
            MessageSegment.image(file=f"file://{os.path.abspath(f'{file_name}.png')}")
        )
    )
    os.remove(f"./{file_name}.png")
