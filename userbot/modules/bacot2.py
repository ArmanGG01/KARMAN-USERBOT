# JANGAN KAU UBAH ANJING 
# BY KARMAN-USERBOT
# KAU ITU KONTOL


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.bacot01(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HEH ANAK ANJING KAU BABI PUKIMAK YATIM LONTE BAJINGAN GA TAU DI UNTUNG,NI KU KASI TAU SAMA KAU YAA KALO KAU ITU BAUK NEREKA JAHANNAM**")


@register(outgoing=True, pattern='^.bacot02(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAU ITU ANAK KONTOL YANG SOK KAYA YANG KENYATAANNYA MISKIN 7 TURUNAN,JADI JANGAN SOK SOKAN SOK KAYA YA PEPEK,DEPAN PACAR KAU,KAU BELAGAK PALING KAYA TAPI SETIBANYA KAU SAMA KAWAN MU SENDIRI MALAH MINJEM UANG ANJING ANJING BANGET**")


@register(outgoing=True, pattern='^.bacot03(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**AHH ENTAH LAH ANJING AKU PUSING MIKIR KATA-KATA LAGI SEENAKNYA PULAK NANTI KAU,NANTI UDAH CAPEK AKU NGETIK KAYA GINI KAI MALAH TINGGAL COPY ABIS ITU KAU JADIKAN BUAT BAHAN WAR GC KAU YANG GAK SEBERAPA ITU**")


@register(outgoing=True, pattern='^.bacot04(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAHAHAHAH DASAR GC AMAPAS YANG ISI NYA KEBANYAKAN LONTE,GAYANYA SI NGAJAK WAR VNV TAPI SETIBANYA DI LADENI MUKA NYA KAYA KONTOL BEDAKI HAHAHAHAH,MENDING KAU SANA MAKE SCARLET BIAR GLOWING EHH JANGAN MAKE SCARLET MAKE PEJU ANAK HARAM AJA BIAR GLOWING 100 TURUNAN MUKA KAU PEPEK HAHAHAHAHAHAHAH**")


@register(outgoing=True, pattern='^.bacot05(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SUMPAH KAU ITU ANAK HARAM YANG DI BUANG KE TONG SAMPAH ABIS ITU DI KUTIP SAMA BAPAK KAU YANG SEKARNG IYA YANG MISKIN JELEK BEDAKI KONTOL BENGKOK**")



CMD_HELP.update({
         "bacot01": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bacot01`"\
        "\n➥ : Untuk Ngebacot Perisi Bot Silahkan Chek Sendiri Dari 01 Sampai 05."})
