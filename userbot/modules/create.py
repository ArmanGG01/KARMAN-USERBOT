from telethon.tl import functions
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.buat (gb|g|c)(?: |$)(.*)")
async def telegraphs(grop):
    """ For .create command, Creating New Group & Channel """
    if grop.text[0].isalpha() or grop.text[0] in ("/", "#", "@", "!"):
        return
    if grop.fwd_from:
        return
    type_of_group = grop.pattern_match.group(1)
    group_name = grop.pattern_match.group(2)
    if type_of_group == "gb":
        try:
            result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@MissRose_bot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            created_chat_id = result.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit(
                f"Grup/Channel {group_name} Berhasil Dibuat. Tekan [{group_name}]({result.link}) Untuk Melihatnya"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))
    elif type_of_group in ["g", "c"]:
        try:
            r = await grop.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about="`Selamat Datang Di Channel Ini!`",
                    megagroup=type_of_group != "c",
                )
            )
            created_chat_id = r.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit(
                f"Grup/Channel {group_name} Berhasil Dibuat. Tekan [{group_name}]({result.link}) Untuk Melihatnya"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))

CMD_HELP.update({
    "membuat": "\
Membuat\
\nUsage: Untuk membuat Channel, Grup dan Grup bersama Bot.\
\n\n`.buat g` <nama grup>\
\nUsage: Membuat grup mu.\
\n\n`.buat gb` <nama grup>\
\nUsage: Membuat Grup bersama bot.\
\n\n`.buat c` <nama channel>\
\nUsage: Membuat sebuah Channel.\
"})
