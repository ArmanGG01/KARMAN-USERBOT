from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.alfatihah(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**SURAT ALFATIHAH**")
    sleep(1)
    await typew.edit("**bismillāhir-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**al-ḥamdu lillāhi rabbil-'ālamīn**")
    sleep(1)
    await typew.edit("**ar-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**māliki yaumid-dīn**")
    sleep(1)
    await typew.edit("**iyyāka na'budu wa iyyāka nasta'īn**")
    sleep(1)
    await typew.edit("**ihdinaṣ-ṣirāṭal-mustaqīm**")
    sleep(1)
    await typew.edit(
        "**ṣirāṭallażīna an'amta 'alaihim gairil-magḍụbi 'alaihim wa laḍ-ḍāllīn**"
    )
    sleep(1)
    await typew.edit("**Amin..**")


@register(outgoing=True, pattren="^.kursi(?: |$)(.*)")
async def typewriter(kursi):
    typew.pattern_match.group(2)
    sleep(2)
    await typew.edit("**NI GUA BACAIIN AYAT KURSI BIAR SETAN DAN JIN KALIAN ILANG**")
    sleep(2)
    await typew.edit("**Alloohu laa ilaaha illaa huwal hayyul qoyyuum**")
    sleep(2)
    await typew.edit("**laa ta’khudzuhuu sinatuw walaa naum**")
    sleep(2)
    await typew.edit("**Lahuu maa fissamaawaati wa maa fil ardli man dzal ladzii yasyfa’u ‘indahuu illaa biidznih**")
    sleep(2)
    await typew.edit(
        "**ya’lamu maa baina aidiihim wamaa kholfahum wa laa yuhiithuuna bisyai’im min ‘ilmihii illaa bimaa syaa’ wasi’a kursiyyuhus samaawaati wal ardlo walaa ya’uuduhuu hifdhuhumaa wahuwal ‘aliyyul ‘adhiim**"
    )
    sleep(2)
    await type.edit("**Aamiin**")


# Create by myself @PakkPoll

CMD_HELP.update(
    {
        "surat": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.alfatihah`\
    \n↳ : Surat Alfatihah."
    }
)
