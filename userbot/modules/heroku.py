"""
   Heroku manager for your rams
"""

import math
import os
import codecs
import aiohttp
import heroku3
import urllib3
import requests

from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME, SUDO_USERS
from userbot.utils import edit_or_reply, edit_delete, kar_cmd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


"""
   ConfigVars setting, get current var, set var or delete var...
"""


@kar_cmd(pattern="(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await edit_or_reply(
            var, "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **di Heroku**"
        )
        return False
    if var.sender_id in SUDO_USERS:
        return
    if exe == "get":
        xx = await edit_or_reply(var, "`Mendapatkan Informasi...`")
        variable = var.pattern_match.group(2)
        if variable == "":
            configvars = heroku_var.to_dict()
            if BOTLOG_CHATID:
                msg = "".join(
                    f"`{item}` = `{configvars[item]}`\n" for item in configvars
                )
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n" "**Config Vars**:\n" f"{msg}"
                )
                await xx.edit("**Berhasil Mengirim Ke BOTLOG_CHATID**")
                return True
            await xx.edit("**Mohon Ubah Var** `BOTLOG` **Ke** `True`")
            return False
        if variable in heroku_var:
            if BOTLOG_CHATID:
                await var.client.send_message(
                    BOTLOG_CHATID,
                    "**Logger : #SYSTEM**\n\n"
                    "**#SET #VAR_HEROKU #ADDED**\n\n"
                    f"`{variable}` **=** `{heroku_var[variable]}`\n",
                )
                await xx.edit("**Berhasil Mengirim Ke BOTLOG_CHATID**")
                return True
            await xx.edit("**Mohon Ubah Var** `BOTLOG` **Ke** `True`")
            return False
        await var.edit("`Informasi Tidak Ditemukan...`")
        return True
    if exe == "del":
        xx = await edit_or_reply(var, "`Menghapus Config Vars...`")
        variable = var.pattern_match.group(2)
        if variable == "":
            await xx.edit(f"**Mohon Tentukan Config Vars Yang Mau Anda Hapus {owner}**")
            return False
        if variable in heroku_var:
            if BOTLOG_CHATID:
                await var.client.send_message(
                    BOTLOG_CHATID,
                    "**Logger : #SYSTEM**\n\n"
                    "**#SET #VAR_HEROKU #DELETED**\n\n"
                    f"`{variable}`",
                )
            await xx.edit(f"**Config Vars Telah Dihapus {owner}**")
            del heroku_var[variable]
        else:
            await xx.edit("**Tidak Dapat Menemukan Config Vars**")
            return True


@kar_cmd(pattern="set var (\w*) ([\s\S]*)")
async def set_var(var):
    if app is None:
        return await edit_or_reply(
            var, "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **dan** `HEROKU_API_KEY`"
        )
    if var.sender_id in SUDO_USERS:
        return
    xx = await edit_or_reply(var, "`Processing...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG_CHATID:
            await var.client.send_message(
                BOTLOG_CHATID,
                "**Logger : #SYSTEM**\n\n"
                "**#SET #VAR_HEROKU #ADDED**\n\n"
                f"`{variable}` = `{value}`",
            )
        await xx.edit("`Sedang Proses, Mohon Tunggu sebentar..`")
    else:
        if BOTLOG_CHATID:
            await var.client.send_message(
                BOTLOG_CHATID,
                "**Logger : #SYSTEM**\n\n"
                "**#SET #VAR_HEROKU #ADDED**\n\n"
                f"`{variable}` **=** `{value}`",
            )
        await xx.edit("**Berhasil Menambahkan Config Var**")
    heroku_var[variable] = value


"""
    Check account quota, remaining quota, used quota, used app quota
"""


@kar_cmd(pattern="(usage|kuota|dyno|kekuatan|paketan)(?: |$)")
async def dyno_usage(dyno):
    if app is None:
        return await dyno.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **dan** `HEROKU_API_KEY`"
        )
    xx = await edit_or_reply(dyno, "`Mengecek Dyno Heroku Anak anjing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/81.0.4044.117 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    async with aiohttp.ClientSession() as session, session.get(
        heroku_api + path, headers=headers
    ) as r:
        if r.status != 200:
            await dyno.client.send_message(
                dyno.chat_id, f"`{r.reason}`", reply_to=dyno.id
            )
            await xx.edit("**Gagal Mendapatkan Informasi Dyno**")
            return False
        result = await r.json()
        quota = result["account_quota"]
        quota_used = result["quota_used"]

        """ - User Quota Limit and Used - """
        remaining_quota = quota - quota_used
        percentage = math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        math.floor(hours / 24)

        """ - User App Used Quota - """
        Apps = result["apps"]
        for apps in Apps:
            if apps.get("app_uuid") == app.id:
                AppQuotaUsed = apps.get("quota_used") / 60
                AppPercentage = math.floor(apps.get("quota_used") * 100 / quota)
                break
        else:
            AppQuotaUsed = 0
            AppPercentage = 0

        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)

        await edit_delete(xx,
                f"𝗜𝗡𝗙𝗢 𝗡𝗚𝗘𝗡𝗧𝗢𝗗!\n\n"
                "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗦𝗔𝗔𝗧 𝗜𝗡𝗜 : \n"
                f"┣•   ▸ {AppHours} ᴊᴀᴍ - {AppMinutes} ᴍᴇɴɪᴛ. \n"
                f"┣•   ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : {AppPercentage}% \n"
                "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                "╼┅━━━━━━━━╍━━━━━━━━┅╾ \n"
                "╭✠╼━━━━━━❖━━━━━━━✠╮ \n"
                "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗕𝗨𝗟𝗔𝗡 𝗜𝗡𝗜 : \n"
                f"┣•  ▸ {hours} ᴊᴀᴍ - {minutes} ᴍᴇɴɪᴛ. \n"
                f"┣•  ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : {percentage}%. \n"
                "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                f"• 𝗣𝗘𝗠𝗜𝗟𝗜𝗞  : ᴀʀᴍᴀɴ \n"
                f"• 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 : [𝗞𝗔𝗥𝗠𝗔𝗡-𝗨𝗦𝗘𝗥𝗕𝗢𝗧](https://t.me/Karc0de) \n", 10
            )
        return True


@kar_cmd(pattern="logs")
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            "`Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var.`"
        )
    await dyno.edit("`Sedang Mengambil Logs Anda`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    fd = codecs.open("logs.txt", "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    await dyno.reply(f"`Ini Logs Heroku Anda :`\n\nPaste Ke: [Nekobin]({url})")
    return os.remove("logs.txt")


CMD_HELP.update({"heroku": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}usage|kuota|dyno|kekuatan|paketan`"
                 "\n↳ : Check Quota Dyno Heroku"
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}set var <NEW VAR> <VALUE>`"
                 "\n↳ : Tambahkan Variabel Baru Atau Memperbarui Variabel"
                 "\nSetelah Menyetel Variabel Tersebut, RAM-UBOT Akan Di Restart secara otomatis."
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}get var atau {cmd}get var <VAR>`"
                 "\n↳ : Dapatkan Variabel Yang Ada, !!PERINGATAN!! Gunakanlah Di Grup Privasi Anda."
                 "\nIni Mengembalikan Semua Informasi Pribadi Anda, Harap berhati-hati."
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}del var <VAR>`"
                 "\n↳ : Menghapus Variabel Yang Ada"
                 "\nSetelah Menghapus Variabel, RAM-UBOT Akan Di Restart secara otomatis."})
