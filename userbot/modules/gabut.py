from platform import uname
from time import sleep

from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA BOTOL**")
    sleep(3)
    await typew.edit("**MUKA LU KAYA KONTOL**")


# Pantun


@register(outgoing=True, pattern="^.salam(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@register(outgoing=True, pattern="^.salam2(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("❌ `Icil wibu`")
    sleep(2)
    await typew.edit("✅ `Icil wibu`")
    sleep(1)
    await typew.edit("❌ `Lia stres`")
    sleep(2)
    await typew.edit("✅ `Lia stres`")
    sleep(1)
    await typew.edit("❌ `Melodi Gajelas`")
    sleep(2)
    await typew.edit("✅ `Melodi Gajelas`")
    sleep(1)
    await typew.edit("❌ `Dila Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `Dila Wibu Sangean`")
    sleep(1)
    await typew.edit("❌ `Jeje Normal`")
    sleep(2)
    await typew.edit("✅ `Jeje Autis`")
    sleep(1)
    await typew.edit(
        "`💢 Cuma Arman Yang Paling Waras, Baik Hati, Dan Tidak Sombong 💢`"
    )


# King Userbot Support


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@register(outgoing=True, pattern=r"^\.virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOOHHHH**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**LU CUMAN BISA LIAT MEMEK AMA KONTOL DOANG**")
    sleep(1.5)
    await typew.edit("**BAHAHAHAHAHBAHABHA**")


@register(outgoing=True, pattern="^.perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja Kontol`")


# Perkenalan


@register(outgoing=True, pattern="^.kursi(?: |$)(.*)")
async def typewriter(typew):
    event.pattern_match.group(1)
    sleep(1)
    await typew.edit("**NI GUA BACAIIN AYAT KURSI BIAR SETAN DAN JIN KALIAN ILANG**")
    sleep(1)
    await typew.edit("**Alloohu laa ilaaha illaa huwal hayyul qoyyuum**")
    sleep(1)
    await typew.edit("**laa ta’khudzuhuu sinatuw walaa naum**")
    sleep(1)
    await typew.edit("**Lahuu maa fissamaawaati wa maa fil ardli man dzal ladzii yasyfa’u ‘indahuu illaa biidznih**")
    sleep(1)
    await event.edit("**ya’lamu maa baina aidiihim wamaa kholfahum wa laa yuhiithuuna bisyai’im min ‘ilmihii illaa bimaa syaa’ wasi’a kursiyyuhus samaawaati wal ardlo walaa ya’uuduhuu hifdhuhumaa wahuwal ‘aliyyul ‘adhiim**")
    sleep(1)
    await typew.edit("**Aamiin**")


# Ayat Kursi


@register(outgoing=True, pattern="^.jembot(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**EH GUA MAU NANYAK?**")
    sleep(1)
    await typew.edit("**JEMBOT KALIAN KERITING GA?**")
    sleep(1)
    await typew.edit("**PASTI IYA KAN🤣**")
    sleep(1)
    await typew.edit("**ENGGAK KAYAK JEMBOT GUA YANG LURUS HAHAAHAHA🤣**")
    sleep(1)
    await typew.edit("**SOALNYA JEMBOT GUA LANGKAH😄**")
    sleep(1)
    await typew.edit("**GA KAYA JEMBOT KALIAN YANG PASARAN😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**UDAH AH TAKUT KALIAN NANGIS MALAH MINTA WAR NANTI😂**")
    sleep(1)
    await typew.edit("**MAAF YA CUMAN BERCANDA😁**")
    sleep(1)
    await typew.edit("**TAPI BO'ONG HIYAHIYAJIYA🤣**")


# Create by myself @PakkPoll


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.salam2`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.jembot`\
        \nUsage : buat ngeledek para jembot\
        \n\n Cmd : `.salam`\
        \nUsage : Untuk Memberi Salam\
        \n\n Cmd : `.kursi`\
        \nUsage : Coba Sendiri Aja\
    "
    }
)
