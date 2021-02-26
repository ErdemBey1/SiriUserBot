# SİRİ USERBOT
from telethon import events
import asyncio
from userbot.events import register

@register(outgoing=True, pattern="^.stat")
async def stat(event):
    await event.edit(f"/stat")
    
