import asyncio
import os
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.gizli ?(.*)")
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
Help = CmdHelp('gizli')
Help.add_command('.gizli (yazacağınız mesaj) (@göndereceğiniz kişi)',  None, 'Bu Mesajı Sadece Seçtiğiniz Kişi Görür Onun Grup İçinde Ondan Başka Kimse Göremez').add()