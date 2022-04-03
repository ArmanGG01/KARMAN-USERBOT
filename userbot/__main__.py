## Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module
from pytgcalls import idle
from telethon.tl.functions.channels import InviteToChannelRequest
from userbot import BOTLOG_CHATID, BOTLOG_MSG, BOT_USERNAME, BOT_VER, LOGS, bot, karblacklist, call_py
from userbot.modules import ALL_MODULES
from userbot.utils.utils import autobot
from userbot.utils.tools import hadeh_ajg


try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    call_py.start()
    user = bot.get_me()
    if user.id in karblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BANYAK TINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK KAU.\nCredits: @PakkPoll"
        )
        sys.exit(1)
    LOGS.info(f"💀KARMAN - USERBOT💀 🌟 V{9.0} [ TELAH DIAKTIFKAN KONTOL ]")
except BaseException as e:


async def ram_ubot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"```💢 KARMAN - USERBOT 𝚄𝙳𝙰𝙷 𝙰𝙺𝚃𝙸𝙵 💢\n\n╼┅━━━━━╍━━━━━┅╾\n❍▹ Branch : 𝙺𝙰𝚁𝙼𝙰𝙽-𝚄𝙱𝙾𝚃\n❍▹ BotVer : 9.0\n❍▹``` Owner : [𝙰𝚁𝙼𝙰𝙽](https://t.me/PakkPoll)\n\n╼┅━━━━━╍━━━━━┅╾\n\n```𝙹𝙰𝙽𝙶𝙰𝙽 𝙺𝙰𝚄 𝙺𝙴𝙻𝚄𝙰𝚁 𝙳𝙰𝚁𝙸 𝙶𝚁𝚄𝙿 𝙺𝚄```\n@obrolansuar\n ```𝙱𝙸𝙰𝚁 𝙺𝙰𝚄 𝚃𝙰𝚄 𝙸𝙽𝙵𝙾,𝙿𝙴𝙿𝙴𝙺.\n ```𝙹𝙸𝙺𝙰 𝙱𝙾𝚃 𝚃𝙸𝙳𝙰𝙺 𝙱𝙸𝚂𝙰  .ping 𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙲𝙷𝙴𝙲𝙺 𝚅𝙸𝚆𝙻𝙾𝙶 𝙿𝙰𝙳𝙰 𝙰𝙺𝚄𝙽 𝙷𝙴𝚁𝙾𝙺𝚄 𝙰𝚃𝙰𝚄 𝙿𝚄𝙽 𝙱𝙸𝚂𝙰 𝙻𝙰𝙽𝙶𝚂𝚄𝙽𝙶 𝙿𝙲 𝙳𝙸 𝙱𝙰𝚆𝙰𝙷 👇",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(autobot())
bot.loop.run_until_complete(ram_ubot_on())
idle()
bot.loop.run_until_complete(hadeh_ajg())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
