from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from emoji import emojize
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from userbot.events import register
from datetime import datetime
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.utils import get_input_location
from userbot.cmdhelp import CmdHelp

# FORKED FROM https://github.com/alcyper/alcyper #
@register(outgoing=True, pattern="^.stats(?: |$)(.*)")
async def info(event):
    await event.edit("`Grup analiz ediliyor...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit("`An unexpected error has occurred.`")
    return
    
    
async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Geçersiz Kanal/Grup`")
            return None
        except ChannelPrivateError:
            await event.reply("`Burası gizli grup ve ya Ben buradan ban yedim.`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Böyle bir süper grup ve ya kanal yok`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply(str(err))
            return None
    return chat_info


async def fetch_info(chat, event):
    # chat.chats is a list so we use get_entity() to avoid IndexError
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1), 
                                                        add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    # No chance for IndexError as it checks for msg_info.messages first
    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    # Same for msg_info.users
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Deleted Account"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Unknown"
        location = str(e)
    
    #this is some spaghetti I need to change
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    
    if admins is None:
        # use this alternative way if chat.full_chat.admins_count is None, works even without being an admin
        try:
            participants_admins = await event.client(GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                                                            offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = "<b>Grup İstatistikleri:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if messages_viewable is not None:
        caption += f"Görünen mesajlar: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"Gönderilen mesajlar: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"Gönderilen mesajlar: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    
CmdHelp('combot').add_command('combot', None, 'Mesaj istatistikleri (combot gibi).').add()
