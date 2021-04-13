# SİRİ USERBOT - PLUGİN

import os
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.cmdhelp import CmdHelp

chat = "@MissRose_bot"

@register(outgoing=True, pattern="^.fstat ?(.*)")
async def fstat(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedstat " + kullanıcı + " " + siri)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Engellenmiş Yeniden Başlatın Tekrar deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedstat " + siri)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Engellenmiş Başlatın Tekrar Deneyin.")


@register(outgoing=True, pattern="^.info ?(.*)")
async def info(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/info " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")


@register(outgoing=True, pattern="^.fedinfo ?(.*)")
async def fedinfo(event):
    if event.fwd_from:
        return
    siri = event.pattern_match.group(1)
    if siri == "" and not event.reply_to_msg_id:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedinfo " + siri)
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")


@register(outgoing=True, pattern="^.myfeds ?(.*)")
async def myfeds(event):
    if event.fwd_from:
        return
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await fedstat.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
            
@register(outgoing=True, pattern="^.fban ?(.*)")
async def fban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fban " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
                
@register(outgoing=True, pattern="^.unfban ?(.*)")
async def unfban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/unfban " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
                
@register(outgoing=True, pattern="^.feddemote ?(.*)")
async def feddemote(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/feddemote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/unfban " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
                
@register(outgoing=True, pattern="^.fpromode ?(.*)")
async def fpromode(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fpromode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fpromode " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
            
CmdHelp('rose').add_command(
    'fstat', '<tag/id>', 'Sadece .fstat Yazarsanız Kendiniz İçin Fban Listesini Verir. \n ID veya @KULLANICI ADI Verirseniz O Kişinin Fban Listesini Verir '
).add_command(
    'info', '<tag/id>', 'Sadece .info Yazarsanız kendiniz için Bilgi verir. \n ID veya @KULLANICI ADI Verirseniz O Kişi İçin Bilgi Veri.'
).add_command(
    'fedinfo', '<fed id>', 'Sadece .fedinfo yazarsanız Sizin Federasyonunuz İçin Bilgi Verir. \n FED İD Girerseniz O Federasyonun Bilgisini Verir'
).add_command(
    'myfeds', 'Hangi Federasyonlardan Yetkinizin Olduğunu Gösterir.'
).add_command(
    'fban', '<tag/id>', 'Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fban atabilirsiniz. '
).add_command(
    'unfban', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fbanını Açabilirsiniz. '
).add_command(
    'fpromote', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fban Yetkisi Verebilirsiniz. '
).add_command(
    'feddemote', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fban yetkisini Alabilirsiniz. \n NOT: BU KOMUTLAR HER YERDE ÇALIŞMAKTADIR ÖZEL MESAJLARDA VER HANGİ BİR GRUPTA KULLANA BİLİRSİNİZ @SiriUserBot '
    
).add()
