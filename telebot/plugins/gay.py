# python 3.7.1

"""Available Commands:
.gay"""


import asyncio

from telebot import CMD_HELP
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "gay":
        await event.edit(input_str)
        animation_chars = [
            "HI",
            "WAIT",
            "WAIT ARE YOU....",
            "WAIT ARE YOU UMH...",
            "HI , WAIT ARE YOU A GAY??😬",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 5])


CMD_HELP.update({"gay": ".gay\nUse - useless."})
