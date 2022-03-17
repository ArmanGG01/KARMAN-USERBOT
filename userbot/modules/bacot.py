# JANGAN KAU UBAH ANJING 
# BY KARMAN-USERBOT
# KAU ITU KONTOL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.bacot1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Sebelumnya ku ucapkan salam dulu,ku hanya ingin ngasi tau kau itu babi  🐖 **")


@register(outgoing=True, pattern='^.bacot2(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Kau itu anak anjing yang lahirnya dari lobah dubur bedaki**")


@register(outgoing=True, pattern='^.bacot3(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Muka kau itu kaya tong sampah dari neraka zahannam**")


@register(outgoing=True, pattern='^.bacot4(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gini ya ku kasi tau kau, sebenarnya kau anak haram,dan mamak kau itu kerjanya dulu cuman open BO make kondom bolong dan lahir lah kau anak haram yang ga tau di untung**")


@register(outgoing=True, pattern='^.bacot5(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Memek kau itu murahan 50k udah bisa kontol masuk ke situ hahahah najis anjing keluarga hina bet hina**")


@register(outgoing=True, pattern='^.bacot6(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAHAHAHAHAH KASIAN ANAK ANJING YANG TERBULY DI SINI,IYA KAU LAH BODO,KAU KAN ANAK ANJING BHAKASSSSSS**")


CMD_HELP.update({
         ""asupan": "**Plugin : **`asupan 1-6`\
        \n\n  •  **Syntax :** `.bacot`\
 }
)
