from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import bot


# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("spaminfo")

# ████████████████████████████████ #

aylar = {
  "Jan": "Ocak",
  "Feb": "Şubat",
  "Mar": "Mart",
  "Apr": "Nisan",
  "May": "Mayıs",
  "June": "Haziran",
  "July": "Temmuz",
  "Aug": "Ağustos",
  "Sep": "Eylül",
  "Oct": "Ekim",
  "Nov": "Kasım",
  "Dec": "Aralık"
  
}
@register(outgoing=True, pattern=r"^.sinfo")
async def sinfos(event):
    await event.edit("🔄")
    chat = "@spambot"
    spamdurumu = None
    async with bot.conversation(chat) as conv:
        try:     
            await conv.send_message("/start")
        except YouBlockedUserError:
            await event.client(UnblockRequest(178220800))
            await conv.send_message("/start")
        await event.client.send_read_acknowledge(conv.chat_id)
        spamdurumu = await conv.get_response()
        if spamdurumu.text.startswith("Dear"):
            getspam = spamdurumu.text.split("until ")[1].split(", ")[0]
            spamgun, spamay, spamyil = getspam.split(" ")[0], aylar[getspam.split(" ")[1]], getspam.split(" ")[2]
            spamsaat = spamdurumu.text.split(":")[0].split(", ")[1] + ":" + spamdurumu.text.split(":")[1].split("UTC.")[0]
            toparla = f"🥲 Spam Tespit Edildi! Spamınız {spamgun} {spamay} {spamyil} {spamsaat}  Tarihinde Bitiyor..."
            await event.edit(toparla)
        elif spamdurumu.text.startswith("Good news"):
            await event.edit(LANG["BIRD"])
        else:
            await event.client.forward_messages(event.chat_id, spamdurumu)
            await event.delete()


dnammonc_dda = CmdHelp('sinfo')
dnammonc_dda.add_command("sinfo", None, "Hesabınızın spam durumunu kontrol edin").add()
