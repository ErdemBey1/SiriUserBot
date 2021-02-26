# SİRİUSERBOT / ERDEM-BEY

from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events

@register(outgoing=True, pattern="^.pixelle")
async def pixelator(event):
    if not event.reply_to_msg_id:
        await event.edit("`Lütfen bir fotoğraf veya sticker'a yanıt verin.`")
        return

    reply_message = await event.get_reply_message() 
    
    if not reply_message.media:
        await event.edit("`Lütfen bir fotoğraf veya sticker'a yanıt verin.`")
        return

    chat = "@pixelatorbot"
    if reply_message.sender.bot:
        await event.edit("`Lütfen gerçekten bir kullanıcının mesajına yanıt verin.`")
        return

    await event.edit("`Fotoğraf pikselleştiriliyor...`")
    async with event.client.conversation(chat) as conv:
        try:     
            await event.client.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await event.reply(f"`Mmmh sanırım` {chat} `engellemişsin. Lütfen engeli aç.`")
            return

        response = await conv.wait_event(events.NewMessage(incoming=True,from_users="@PixelatorBot"))
        await event.client.send_read_acknowledge("@PixelAtorBot")
        if response.text.startswith("Looks"):
            await event.edit("`Bunu pikselleştiremem!`")
        else:
            await event.client.send_message(event.chat_id, "`Fotoğraf başarıyla pikselleştirildi!`", file=response.message)
            await event.delete()
