from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk**")


@register(outgoing=True, pattern='^.man(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Saya Jelek❎**")
    await typew.edit("**Saya Ganteng✅**")
    sleep(1)
    await typew.edit("**Saya Punya Ayah❎**")
    await typew.edit("**Saya Tidak Punya Ayah✅**")
    sleep(2)
    await typew.edit("**Pilih Perawan❎**")
    await typew.edit("**Pilih Janda Anak 1✅**")
    sleep(2)
    await typew.edit("**Aku Alay❎**")
    await typew.edit("**Kalian Yang Alay✅**")
    sleep(2)
    await typew.edit("**Virtual❎**")
    await typew.edit("**Real Life✅**")
    sleep(2)
    await typew.edit("**Bapa Lo Orang Kaya❎**")
    await typew.edit("**Bapa Lo Orang Miskin✅**")
    sleep(2)
    await typew.edit("**Hobi Vcs❎**")
    await typew.edit("**Hobi Ngentod✅**")
    sleep(2)
    await typew.edit("**Arman Jahat❎**")
    await typew.edit("**Arman Baik✅**")
    sleep(3)
    await typew.edit("**CUMAN TUAN ARMAN YANG PALING BENER**")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo KONTOL?`")
    sleep(1)
    await typew.edit("`Apa Ga Suka?`")
    sleep(1)
    await typew.edit("`Yahahaha Kasian Bocah Autis`")
    sleep(1)
    await typew.edit("`Ups Sorry Ga sengaja 😂`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")

CMD_HELP.update({
    "karmanubot":
    "`.karmanubot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.man`\
    \nUsage: misi."
})
