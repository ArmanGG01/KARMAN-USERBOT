# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

# port to userbot from uniborg by @keselekpermen69


import io
import re

import userbot.modules.sql_helper.blacklist_sql as sql
from userbot import CMD_HELP
from userbot.events import register


@register(incoming=True, disable_edited=True, disable_errors=True)
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.reply("`Anda Tidak Punya Izin Untuk Menghapus Pesan Disini`")
                await sleep(1)
                await reply.delete()
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@register(outgoing=True, pattern=r"^\.addbl(?: |$)(.*)")
async def on_add_black_list(addbl):
    text = addbl.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(addbl.chat_id, trigger.lower())
    await addbl.edit(
        f"`Menambahkan Kata` **{text}** `Ke Blacklist Untuk Obrolan Ini`"
    )


@register(outgoing=True, pattern=r"^\.listbl(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "`Tidak Ada Blacklist Dalam Obrolan Ini.`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Blacklist Dalam Obrolan Ini",
                reply_to=listbl,
            )
            await listbl.delete()
    else:
        await listbl.edit(OUT_STR)


@register(outgoing=True, pattern=r"^\.manbl(?: |$)(.*)")
async def on_delete_blacklist(manbl):
    text = rmbl.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    if successful := sum(
        1
        for trigger in to_unblacklist
        if sql.rm_from_blacklist(manbl.chat_id, trigger.lower())
    ):
        await manbl.edit(f"`Berhasil Menghapus` **{text}** `Di Blacklist`")
    else:
        await manbl.edit(f"`Maaf,` **{text}** `Tidak Ada Di Blacklist`")


CMD_HELP.update({"blacklist": ">`.listbl`"
                 "\nUsage: Melihat daftar blacklist yang aktif di obrolan."
                 "\n\n>`.addbl <kata>`"
                 "\nUsage: Memasukan pesan ke blacklist 'kata blacklist'."
                 "\nlord bot akan otomatis menghapus 'kata blacklist'."
                 "\n\n>`.rmbl <kata>`"
                 "\nUsage: Menghapus kata blacklist."})
