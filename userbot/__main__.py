""" Userbot start point """


import sys
import requests
from importlib import import_module

from pytgcalls import idle

from userbot import BOT_TOKEN, BOT_VER, karblacklist
from userbot import DEVS, LOGS, LOOP, bot, call_py, BOTLOG_CHATID
from userbot.clients import ram_ubot_on, ramulti
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, creatgr, hadeh_ajg

try:
    client = ramulti()
    total = 5 - client
    bot.start()
    call_py.start()
    user = bot.get_me()
    ramblacklist = requests.get(
        "https://raw.githubusercontent.com/ArmanGG01/Karblack/master/karblacklist.json"
    ).json()
    if user.id in ramblacklist:
        LOGS.warning(
            "USERBOT TIDAK DAPAT BERJALAN, KARNA LO KONTOL MAKE SEMEMA MENA, BOT LO DI MATIIN HEHEH, LAPORKAN KE @MERDHNI"        )
        sys.exit(1)
    if 1694909518 not in DEVS:
        LOGS.warning(
            f"EOL\n✨ KARMAN - USERBOT ✨ versi {9.0}, © copyright by @merdhni"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(f"Total Clients = {total} User")
LOGS.info(f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/obrolansuar")
LOGS.info(f"✨ KARMAN - USERBOT ✨ v {9?0} [UDAH AKTIF KONTOL]")


LOOP.run_until_complete(ram_ubot_on())
LOOP.run_until_complete(hadeh_ajg())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(creatgr())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
