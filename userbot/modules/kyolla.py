import asyncio
import telethon
from userbot.events import register
from telethon import events
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.kyolla")
async def tm(event):
  if event.is_reply:
    mesaj = await event.get_reply_message()
  else:
    await event.edit("`Bir mesaja yanıt verin!`")
    return
  await event.client.forward_messages("me", mesaj)
  await event.edit("`Mesaj` Siri __Kayıtlı Mesajlar__ `Bölümüne Yolladı`")
  
CmdHelp('kyolla').add_command('kyolla', '<bir mesaja yanıt verin>', 'Yanıt verdiyiniz mesajı Kayıtlı Mesajlar(Saved Messages) bölümüne gönderir.').add()