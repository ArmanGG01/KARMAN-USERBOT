""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.rhelp` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[LANDAK🦔](t.me/teman_random)"
        "\n\n[SUPPORT](https://t.me/geezsupportgroup)"
        "\n\n[CHANNEL](https://t.me/ramubotinfo)")


@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ramadhani892/RAM-UBOT/RAM-UBOT/varshelper.txt)")


CMD_HELP.update({
    "ramhelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk RAM-UBOT.\
\n`.rvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
