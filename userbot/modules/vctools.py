import asyncio
from pytgcalls import StreamType as ya
from pytgcalls.types.input_stream import AudioPiped as kartod
from pytgcalls.exceptions import (
    NoActiveGroupCall as memek,
    AlreadyJoinedError as asu,
    NotInGroupCallError as ajg
)
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest as ngentod
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, call_py
from userbot.utils import edit_delete, edit_or_reply, edit_delete, kar_cmd
from userbot.events import register as tod

from userbot.utils.queues.queues import clear_queue

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"



# credits by @vckyaz < vicky \>
# recode by @lahsiajg < starboy \>
# ex by OpyRights

@kar_cmd(pattern="joinvc(?: |$)(.*)")
@tod(pattern="^\.cjoinvc(?: |$)(.*)")
async def join_(event):
    await edit_or_reply(event, f"**processing....**")
    if len(event.text.split()) > 1:
        chat = event.chat_id
        chats = event.pattern_match.group(1)
        try:
            chat = await event.client(ngentod(chats))
        except asu as e:
            await call_py.leave_group_call(chat)
            clear_queue(chat)
            await asyncio.sleep(3)
            return await edit_delete(event, f"**ERROR:** `{e}`", 30)
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return await edit_or_reply(event, "NodeJs is not installed or installed version is too old.")
    else:
        chat_id = event.chat_id
        chats = event.pattern_match.group(1)
        vcmention(event.sender)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat_id,
        kartod(
            'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
        ),
        chats,
        stream_type=ya().pulse_stream,
    )
    await edit_delete(event, f"**Berhasil Join OS Jamet.**\n**ID:{chat_id}**", 5)


@kar_cmd(pattern="leavevc(?: |$)(.*)")
@tod(pattern=r"^\.cleavevc(?: |$)(.*)")
async def leavevc(event):
    """ leave video chat """
    await edit_or_reply(event, "**processing....**")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if from_user:
        try:
            await call_py.leave_group_call(chat_id)
        except (memek, ajg):
            await edit_or_reply(event, f"Woy {from_user}, Kontol Kau Ga Ada Di OS")
        await edit_delete(event, f"**Di OS Banyak Jamet Jadi, {from_user} Mau Turun Hahaha **", 2)

CMD_HELP.update(
    {
        "joinvc": f"**Plugin : **`joinvc`\
        \n\n  •  **Syntax :** `{cmd}joinvc`\
        \n  •  **Function : **Untuk Naik Ke Dalam Obrolan Suara Jamet.\
        \n\n  •  **Syntax :** `{cmd}leavevc`\
        \n  •  **Function : **Untuk Turun Dari Obrolan Suara Jamet.\
    "
    }
)
