# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
# recode by @greyyvbss


import random

from userbot import CMD_HELP
from userbot.events import register
from userbot import DEFAULTUSER
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@balabalabotbokep", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Ini Asupannya Buat Kau [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video orang colmek.")

@register(outgoing=True, pattern=r"^\.desah$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Ini Desahanya Buat Kau [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan vn desahan.")
        
@register(outgoing=True, pattern=r"^\.ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Ini Ayang Kau [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Gada Yang Mau Sama Kamu Karena Kau Jelek🤪.")

@register(outgoing=True, pattern=r"^\.cayang$")
async def _(event):
    try:
        gantengnya = [
            ganteng
            async for ayang in event.client.iter_messages(
                "@Cowogantenghalu", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Nih Pacar Aku 😘 [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Gada Yang Mau Sama Kamu Karena Kau Jelek🤪.")


CMD_HELP.update(
    {
        "asupan": "**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `.asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `.desah`\
        \n  •  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
        \n\n  •  **Syntax :** `.ayang`\
        \n  •  **Function : **Untuk Mencari ayang buat cowok yang jomblo.\
        \n\n  •  **Syntax :** `.cayang`\
        \n  •  **Function : **Untuk Mencari ayang buat cewek yang jomblo.\
    "
    }
)
