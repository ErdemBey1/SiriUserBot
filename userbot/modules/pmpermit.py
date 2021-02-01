# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Asena UserBot - Yusuf Usta


""" Kimin size özel mesaj gönderebileceğini kontrol altına almanızı sağlayan UserBot modülüdür. """

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.types import User
from sqlalchemy.exc import IntegrityError

from userbot import (COUNT_PM, CMD_HELP, BOTLOG, BOTLOG_CHATID,
                     PM_AUTO_BAN, PM_AUTO_BAN_LIMIT, LASTMSG, LOGS, BRAIN_CHECKER, WHITELIST)
from userbot.events import register
from userbot.main import PLUGIN_MESAJLAR
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("pmpermit")

# ████████████████████████████████ #

@register(incoming=True, disable_edited=True, disable_errors=True)
async def permitpm(event):
    """ İzniniz olmadan size PM gönderenleri yasaklamak içindir. \
        Yazmaya devam eden kullanıcıları engeller. """
    if PM_AUTO_BAN:
        self_user = await event.client.get_me()
        if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (
                await event.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                from userbot.modules.sql_helper.globals import gvarstatus
            except AttributeError:
                return
            apprv = is_approved(event.chat_id)
            notifsoff = gvarstatus("NOTIF_OFF")

            reply_user = await event.get_sender()
            id = reply_user.id
            first_name = str(reply_user.first_name)
            if reply_user.last_name:
                last_name = str(reply_user.last_name)
            else:
                last_name = ''

            username = '@' + reply_user.username if reply_user.username else f'[{first_name} {last_name}](tg://user?id={id})'
            mention = f'[{first_name} {last_name}](tg://user?id={id})'

            # Bu bölüm basitçe akıl sağlığı kontrolüdür.
            # Eğer mesaj daha önceden onaylanmamış olarak gönderildiyse
            # flood yapmayı önlemek için unapprove mesajı göndermeyi durdurur.
            if not apprv and event.text != PLUGIN_MESAJLAR['pm']:
                if event.chat_id in LASTMSG:
                    prevmsg = LASTMSG[event.chat_id]
                    # Eğer önceden gönderilmiş mesaj farklıysa unapprove mesajı tekrardan gönderilir.
                    if event.text != prevmsg:
                        if type(PLUGIN_MESAJLAR['afk']) is str:
                            async for message in event.client.iter_messages(
                                event.chat_id,
                                from_user='me',
                                search=PLUGIN_MESAJLAR['pm'].format(
                                    id=id,
                                    username=username,
                                    mention=first_name,
                                    first_name=first_name,
                                    last_name=last_name
                                )
                            ):
                                await message.delete()
                            await event.reply(PLUGIN_MESAJLAR['pm'].format(
                                id=id,
                                username=username,
                                mention=mention,
                                first_name=first_name,
                                last_name=last_name
                            ))
                        else:
                            async for message in event.client.iter_messages(
                                event.chat_id,
                                from_user='me',
                                limit=PM_AUTO_BAN_LIMIT + 1):
                                    await message.delete()
                            if not PLUGIN_MESAJLAR['pm'].text == '':
                                PLUGIN_MESAJLAR['pm'].text = PLUGIN_MESAJLAR['pm'].text.format(
                                    id=id,
                                    username=username,
                                    mention=mention,
                                    first_name=first_name,
                                    last_name=last_name
                                )

                            await event.reply(PLUGIN_MESAJLAR['pm'])
                    LASTMSG.update({event.chat_id: event.text})
                else:
                    await event.reply(PLUGIN_MESAJLAR['pm'].format(
                                    id=id,
                                    username=username,
                                    mention=mention,
                                    first_name=first_name,
                                    last_name=last_name
                                ))
                    LASTMSG.update({event.chat_id: event.text})

                if notifsoff:
                    await event.client.send_read_acknowledge(event.chat_id)
                if event.chat_id not in COUNT_PM:
                    COUNT_PM.update({event.chat_id: 1})
                else:
                    COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1

                if COUNT_PM[event.chat_id] > PM_AUTO_BAN_LIMIT:
                    await event.respond(
                        LANG['BLOCKED']
                    )

                    try:
                        del COUNT_PM[event.chat_id]
                        del LASTMSG[event.chat_id]
                    except KeyError:
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                LANG['ERROR'],
                            )
                        LOGS.info(
                            LANG['ERROR'])
                        return

                    await event.client(BlockRequest(event.chat_id))
                    await event.client(ReportSpamRequest(peer=event.chat_id))

                    if BOTLOG:
                        name = await event.client.get_entity(event.chat_id)
                        name0 = str(name.first_name)
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            "[" + name0 + "](tg://user?id=" +
                            str(event.chat_id) + ")" +
                            LANG['BOTLOG_BLOCKED'],
                        )

@register(disable_edited=True, outgoing=True, disable_errors=True)
async def auto_accept(event):
    """ İlk mesajı atan sizseniz otomatik olarak onaylanır. """
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (
            await event.get_sender()).bot:
        try:
            from userbot.modules.sql_helper.pm_permit_sql import is_approved
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except AttributeError:
            return

        chat = await event.get_chat()
        id = chat.id
        first_name = str(chat.first_name)
        if chat.last_name:
            last_name = str(chat.last_name)
        else:
            last_name = ''

        username = '@' + chat.username if chat.username else f'[{first_name} {last_name}](tg://user?id={id})'
        mention = f'[{first_name} {last_name}](tg://user?id={id})'

        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(event.chat_id,
                                                            reverse=True,
                                                            limit=1):
                if type(PLUGIN_MESAJLAR['afk']) is str:
                    if message.message is not PLUGIN_MESAJLAR['pm'].format(
                                    id=id,
                                    username=username,
                                    mention=mention,
                                    first_name=first_name,
                                    last_name=last_name
                                ) and message.from_id == self_user.id:
                        try:
                            approve(event.chat_id)
                        except IntegrityError:
                            return
                else:
                    if message is not PLUGIN_MESAJLAR['pm'] and message.from_id == self_user.id:
                        try:
                            approve(event.chat_id)
                        except IntegrityError:
                            return


                if is_approved(event.chat_id) and BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#OTOMATIK-ONAYLANDI\n" + "Kullanıcı: " +
                        f"[{chat.first_name}](tg://user?id={chat.id})",
                    )


@register(outgoing=True, pattern="^.notifoff$")
async def notifoff(noff_event):
    """ .notifoff komutu onaylanmamış kişilerden gelen PM lerden bildirim almamanızı sağlar. """
    try:
        from userbot.modules.sql_helper.globals import addgvar
    except AttributeError:
        await noff_event.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    addgvar("NOTIF_OFF", True)
    await noff_event.edit(LANG['NOTIFOFF'])


@register(outgoing=True, pattern="^.notifon$")
async def notifon(non_event):
    """ .notifon komutu onaylanmamış kişilerden gelen PM lerden bildirim almanızı sağlar. """
    try:
        from userbot.modules.sql_helper.globals import delgvar
    except:
        await non_event.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    delgvar("NOTIF_OFF")
    await non_event.edit(LANG['NOTIFON'])


@register(outgoing=True, pattern="^.approve$")
async def approvepm(apprvpm):
    """ .approve komutu herhangi birine PM atabilme izni verir. """
    try:
        from userbot.modules.sql_helper.pm_permit_sql import approve
    except:
        await apprvpm.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return

    if apprvpm.reply_to_msg_id:
        reply = await apprvpm.get_reply_message()
        reply_user = await apprvpm.client.get_entity(reply.from_id)
    else:
        reply_user = await apprvpm.client.get_entity(apprvpm.chat_id)

    id = reply_user.id
    first_name = str(reply_user.first_name)
    if reply_user.last_name:
        last_name = str(reply_user.last_name)
    else:
        last_name = ''

    username = '@' + reply_user.username if reply_user.username else f'[{first_name} {last_name}](tg://user?id={id})'
    mention = f'[{first_name} {last_name}](tg://user?id={id})'

    try:
        approve(id)
    except IntegrityError:
        await apprvpm.edit(LANG['ALREADY'])
        return

    await apprvpm.edit(PLUGIN_MESAJLAR['approve'].format(
        id=id,
        username=username,
        mention=mention,
        first_name=first_name,
        last_name=last_name
    ))
    async for message in apprvpm.client.iter_messages(apprvpm.chat_id,
                                                      from_user='me',
                                                      search=PLUGIN_MESAJLAR['pm'].format(
        id=id,
        username=username,
        mention=first_name,
        first_name=first_name,
        last_name=last_name
    )):
        await message.delete()

    if BOTLOG:
        await apprvpm.client.send_message(
            BOTLOG_CHATID,
            "#ONAYLANDI\n" + "Kullanıcı: " + mention,
        )


@register(outgoing=True, pattern="^.disapprove$")
async def disapprovepm(disapprvpm):
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
    except:
        await disapprvpm.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return

    if disapprvpm.reply_to_msg_id:
        reply = await disapprvpm.get_reply_message()
        replied_user = await disapprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        dissprove(replied_user.id)
    else:
        dissprove(disapprvpm.chat_id)
        aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
        name0 = str(aname.first_name)

    await disapprvpm.edit(PLUGIN_MESAJLAR['disapprove'].format(mention = f"[{name0}](tg://user?id={disapprvpm.chat_id})"))

    if BOTLOG:
        await disapprvpm.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={disapprvpm.chat_id})"
            " kişisinin PM atma izni kaldırıldı.",
        )


@register(outgoing=True, pattern="^.block$")
async def blockpm(block):
    """ .block komutu insanları engellemenizi sağlar. """
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client.get_entity(reply.from_id)
        if replied_user.id in BRAIN_CHECKER or replied_user.id in WHITELIST:
            await block.edit(
                "`Oups, Xəta! Bağışla amma bunu SpaceAI'də səlahiyyətli birinə edə bilmərəm 👨‍🚀!!`"
            )
            return

        id = replied_user.id
        first_name = str(replied_user.first_name)
        if replied_user.last_name:
            last_name = str(replied_user.last_name)
        else:
            last_name = ''

        username = '@' + replied_user.username if replied_user.username else f'[{first_name} {last_name}](tg://user?id={id})'
        mention = f'[{first_name} {last_name}](tg://user?id={id})'
        await block.client(BlockRequest(replied_user.id))
        await block.edit(PLUGIN_MESAJLAR['block'].format(
            id=id,
            username=username,
            mention=mention,
            first_name=first_name,
            last_name=last_name
        ))
    else:
        if block.chat_id in BRAIN_CHECKER:
            await block.edit(
                "`Oups, Xəta! Bağışla amma bunu SpaceAI Sahibinə edə bilmərəm 👨‍🚀!!`"
            )
            return

        await block.client(BlockRequest(block.chat_id))
        replied_user = await block.client.get_entity(block.chat_id)
        id = replied_user.id
        first_name = str(replied_user.first_name)
        if replied_user.last_name:
            last_name = str(replied_user.last_name)
        else:
            last_name = ''

        username = '@' + replied_user.username if replied_user.username else f'[{first_name} {last_name}](tg://user?id={id})'
        mention = f'[{first_name} {last_name}](tg://user?id={id})'

        await block.edit(PLUGIN_MESAJLAR['block'].format(
            id=id,
            username=username,
            mention=mention,
            first_name=first_name,
            last_name=last_name
        ))
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
        dissprove(id)
    except:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            "#ENGELLENDI\n" + "Kullanıcı: " + mention,
        )


@register(outgoing=True, pattern="^.unblock$")
async def unblockpm(unblock):
    """ .unblock komutu insanların size yeniden PM atabilmelerini sağlar. """
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.from_id)
        name0 = str(replied_user.first_name)
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit(f"`{LANG['UNBLOCKED']}`")

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={replied_user.id})"
            " kişisinin engeli kaldırıldı.",
        )

CmdHelp('pmpermit').add_command(
    'approve', None, 'Cavab verilən istifadəçiyə PM yazma icazəsi verilir.', 
).add_command(
    'disapprove', None, 'Cavab verilən istifadəçinin PM icasəsini alar.'
).add_command(
    'block', '<istifadəçi adı/cavablama>', 'İstifadəçini blok edər.'
).add_command(
    'unblock', '<istifadəçi adş/cavablama>', 'İstifadəçini blokdar çıxarar.'
).add_command(
    'notifoff', None, 'İcazə verilmiş şəxsi mesajların bildirimlərini təmizləyər ya da deaktiv edər.'
).add_command(
    'notifon', None, 'İcazə verilmiş şəxsi mesajların bildirim göndərməsinə icazə verər.'
).add()
