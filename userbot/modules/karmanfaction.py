# Port By @VckyouuBitch From Geez-Projects
# # Copyright (C) 2021 Geez-Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(arman):
    t = arman.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await landak.ban_time(t)
            except BaseException:
                return await arman.edit("`Incorrect Format`")
    await arman.edit("`Kebanyakan fake hidup lu ngentot!`")
    await arman.edit(f"`Memulai Fake Typing {t} detik.`")
    async with arman.client.action(arman.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(arman):
    t = arman.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await landak.ban_time(t)
            except BaseException:
                return await arman.edit("`Incorrect Format`")
    await arman.edit(f"`Memulai Fake Audio dalam {t} detik.`")
    async with arman.client.action(arman.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(arman):
    t = arman.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await arman.ban_time(t)
            except BaseException:
                return await arman.edit("`Incorrect Format`")
    await arman.edit(f"`Memulai Fake video dalam {t} detik.`")
    async with arman.client.action(arman.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(arman):
    t = arman.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await arman.ban_time(t)
            except BaseException:
                return await arman.edit("`Incorrect Format`")
    await arman.edit(f"`Memulai Fake Play game dalam {t} detik.`")
    async with landak.client.action(arman.chat_id, "game"):
        await asyncio.sleep(t)

CMD_HELP.update(
    {
        "faction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ftyping : .faudio : .fvideo : .fgame <jumlah text>`"
        "\n• : Fake action ini Berfungsi dalam group"
    }
)
