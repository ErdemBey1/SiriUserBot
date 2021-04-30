# SiriUserBot - ErdemBey - Berceste - Midy
import asyncio
import telethon
from userbot.events import register
from telethon import events
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("kyolla")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.kyolla")
async def tm(event):
  if event.is_reply:
    mesaj = await event.get_reply_message()
  else:
    await event.edit(LANG["REPLY_MESSAGE"])
    return
  await event.client.forward_messages("me", mesaj)
  await event.edit(LANG["SUCCESSFUL"])
  
CmdHelp('kyolla').add_command('kyolla', '<bir mesaja yanıt verin>', 'Yanıt verdiyiniz mesajı Kayıtlı Mesajlar(Saved Messages) bölümüne gönderir.').add()
