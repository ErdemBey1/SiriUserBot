# Copyright (C) 2020 Thanks to Yusuf Usta.
#
# Licensed under the  GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# SiriUserBot - ErdemBey - Berceste - Midy

import re
import os
import sys
from telethon.tl.types import DocumentAttributeFilename, InputMessagesFilterDocument
import importlib
import time
import traceback

from userbot import CMD_HELP, bot, tgbot, PLUGIN_CHANNEL_ID, PATTERNS, BOTLOG, BOTLOG_CHATID, ASISTAN, MYID
from userbot.events import register
from userbot.main import extractCommands
import userbot.cmdhelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__plugin")
LANGG = get_value("misc")

# ████████████████████████████████ #

# Plugin Porter - UniBorg
@register(outgoing=True, pattern="^.pport")
async def pport(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        await event.edit(LANG["REPLY_FOR_PORT"])
        return

    await event.edit(LANG["DOWNLOADING"])
    dosya = await event.client.download_media(reply_message)
    dosy = open(dosya, "r").read()

    borg1 = r"(@borg\.on\(admin_cmd\(pattern=\")(.*)(\")(\)\))"
    borg2 = r"(@borg\.on\(admin_cmd\(pattern=r\")(.*)(\")(\)\))"
    borg3 = r"(@borg\.on\(admin_cmd\(\")(.*)(\")(\)\))"

    if re.search(borg1, dosy):
        await event.edit(LANG["UNIBORG"])
        komu = re.findall(borg1, dosy)

        if len(komu) > 1:
            await event.edit(LANG["TOO_MANY_PLUGIN"])

        komut = komu[0][1]
        degistir = dosy.replace('@borg.on(admin_cmd(pattern="' + komut + '"))', '@register(outgoing=True, pattern="^.' + komut + '")')
        degistir = degistir.replace("from userbot.utils import admin_cmd", "from userbot.events import register")
        degistir = re.sub(r"(from uniborg).*", "from userbot.events import register", degistir)
        degistir = degistir.replace("def _(event):", "def port_" + komut + "(event):")
        degistir = degistir.replace("borg.", "event.client.")
        ported = open(f'port_{dosya}', "w").write(degistir)

        await event.edit(LANG["UPLOADING"])

        await event.client.send_file(event.chat_id, f"port_{dosya}")
        os.remove(f"port_{dosya}")
        os.remove(f"{dosya}")
    elif re.search(borg2, dosy):
        await event.edit(LANG["UNIBORG2"])
        komu = re.findall(borg2, dosy)

        if len(komu) > 1:
            await event.edit(LANG["TOO_MANY_PLUGIN"])
            return

        komut = komu[0][1]

        degistir = dosy.replace('@borg.on(admin_cmd(pattern=r"' + komut + '"))', '@register(outgoing=True, pattern="^.' + komut + '")')
        degistir = degistir.replace("from userbot.utils import admin_cmd", "from userbot.events import register")
        degistir = re.sub(r"(from uniborg).*", "from userbot.events import register", degistir)
        degistir = degistir.replace("def _(event):", "def port_" + komut + "(event):")
        degistir = degistir.replace("borg.", "event.client.")
        ported = open(f'port_{dosya}', "w").write(degistir)

        await event.edit(LANG["UPLOADING"])

        await event.client.send_file(event.chat_id, f"port_{dosya}")
        os.remove(f"port_{dosya}")
        os.remove(f"{dosya}")
    elif re.search(borg3, dosy):
        await event.edit(LANG["UNIBORG3"])
        komu = re.findall(borg3, dosy)

        if len(komu) > 1:
            await event.edit(LANG["TOO_MANY_PLUGIN"])
            return

        komut = komu[0][1]

        degistir = dosy.replace('@borg.on(admin_cmd("' + komut + '"))', '@register(outgoing=True, pattern="^.' + komut + '")')
        degistir = degistir.replace("from userbot.utils import admin_cmd", "from userbot.events import register")
        degistir = re.sub(r"(from uniborg).*", "from userbot.events import register", degistir)
        degistir = degistir.replace("def _(event):", "def port_" + komut.replace("?(.*)", "") + "(event):")
        degistir = degistir.replace("borg.", "event.client.")

        ported = open(f'port_{dosya}', "w").write(degistir)

        await event.edit(LANG["UPLOADING"])

        await event.client.send_file(event.chat_id, f"port_{dosya}")
        os.remove(f"port_{dosya}")
        os.remove(f"{dosya}")

    else:
        await event.edit(LANG["UNIBORG_NOT_FOUND"])

@register(outgoing=True, pattern="^.plist")
async def plist(event):
    if PLUGIN_CHANNEL_ID != None:
        await event.edit(LANG["PLIST_CHECKING"])
        yuklenen = f"{LANG['PLIST']}\n\n"
        async for plugin in event.client.iter_messages(PLUGIN_CHANNEL_ID, filter=InputMessagesFilterDocument):
            try:
                dosyaismi = plugin.file.name.split(".")[1]
            except:
                continue

            if dosyaismi == "py":
                yuklenen += f"🌈 {plugin.file.name}\n"
        try:
            await event.edit(yuklenen)
        except:
            await event.reply(yuklenen)
    else:
        try:
            await event.edit(LANG["TEMP_PLUGIN"])
        except:
            await event.reply(LANG["TEMP_PLUGIN"])


@register(incoming=True, from_users=ASISTAN, pattern="^.plist")
async def plistasistan(ups):
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            usp = await event.reply(LANG["PLIST_CHECKING"])
            yuklenen = f"{LANG['PLIST']}\n\n"
            async for plugin in event.client.iter_messages(PLUGIN_CHANNEL_ID, filter=InputMessagesFilterDocument):
                try:
                    dosyaismi = plugin.file.name.split(".")[1]
                except:
                    continue

                if dosyaismi == "py":
                    yuklenen += f"🌈 {plugin.file.name}\n"
            await usp.edit(yuklenen)
        else:
            await usp.edit(LANG["TEMP_PLUGIN"])
    else:
        return

@register(outgoing=True, pattern="^.pinstall")
async def pins(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        await event.edit(LANG["REPLY_TO_FILE"])
        return

    await event.edit(LANG["DOWNLOADING"])
    edizin = f"./userbot/modules/{reply_message.file.name}"

    if os.path.exists(edizin):
        await event.edit(LANG["ALREADY_INSTALLED"])
        return

    dosya = await event.client.download_media(reply_message, "./userbot/modules/")

    try:
        spec = importlib.util.spec_from_file_location(dosya, dosya)
        mod = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(mod)
    except Exception as e:
        await event.edit(f"{LANG['PLUGIN_BUGGED']} {e}`")
        return os.remove("./userbot/modules/" + dosya)

    dosy = open(dosya, "r").read()
    if re.search(r"@tgbot\.on\(.*pattern=(r|)\".*\".*\)", dosy):
        komu = re.findall(r"\(.*pattern=(r|)\"(.*)\".*\)", dosy)
        komutlar = ""
        i = 0
        while i < len(komu):
            komut = komu[i][1]
            CMD_HELP["tgbot_" + komut] = f"{LANG['PLUGIN_DESC']} {komut}"
            komutlar += komut + " "
            i += 1
        await event.edit(LANG['PLUGIN_DOWNLOADED'] % komutlar)
    else:
        Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", dosy)

        if (not type(Pattern) == list) or (len(Pattern) < 1 or len(Pattern[0]) < 1):
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                return await event.edit(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımını Öğrenmek İçin__ `.siri {cmdhelp}` __yazın.__')
            else:
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                userbot.cmdhelp.CmdHelp(dosya).add_warning('Komutlar bulunamadı!').add()
                return await event.edit(LANG['PLUGIN_DESCLESS'])
        else:
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                return await event.edit(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımını Öğrenmek İçin__ `.siri {cmdhelp}` __yazın.__')
            else:
                dosyaAdi = reply_message.file.name.replace('.py', '')
                extractCommands(dosya)
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                return await event.edit(f'**Modül Başarıyla Yüklendi**\n__Modülün  Kullanımını Öğrenmek İçin__ `.siri {dosyaAdi}` __yazın.__')

@register(outgoing=True, pattern="^.ptest")
async def ptest(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        await event.edit(LANG["REPLY_TO_FILE"])
        return

    await event.edit(LANG["DOWNLOADING"])
    if not os.path.exists('./userbot/temp_plugins/'):
        os.makedirs('./userbot/temp_plugins')
    dosya = await event.client.download_media(reply_message, "./userbot/temp_plugins/")
    
    try:
        spec = importlib.util.spec_from_file_location(dosya, dosya)
        mod = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(mod)
    except Exception as e:
        await event.edit(f"{LANG['PLUGIN_BUGGED']} {e}`")
        return os.remove("./userbot/temp_plugins/" + dosya)

    return await event.edit(f'**Modül Başarıyla Yüklendi!**\
    \n__Modülü Test Edebilirsiniz. Botu yeniden başlattığınızda plugin silinecektir.__')

@register(outgoing=True, pattern="^.psend ?(.*)")
async def psend(event):
    modul = event.pattern_match.group(1)
    if len(modul) < 1:
        await event.edit(LANG['PREMOVE_GIVE_NAME'])
        return

    if os.path.isfile(f"./userbot/modules/{modul}.py"):
        await event.client.send_file(event.chat_id, f"./userbot/modules/{modul}.py", caption=LANG['SIRI_PLUGIN_CAPTION'])
        await event.delete()
    else:
        await event.edit(LANG['NOT_FOUND_PLUGIN'])


@register(outgoing=True, pattern="^.premove ?(.*)")
async def premove(event):
    modul = event.pattern_match.group(1).lower()
    if len(modul) < 1:
        await event.edit(LANG['PREMOVE_GIVE_NAME'])
        return

    await event.edit(LANG['PREMOVE_DELETING'])
    i = 0
    a = 0
    async for message in event.client.iter_messages(PLUGIN_CHANNEL_ID, filter=InputMessagesFilterDocument, search=modul):
        await message.delete()
        try:
            os.remove(f"./userbot/modules/{message.file.name}")
        except FileNotFoundError:
            await event.reply(LANG['ALREADY_DELETED'])

        i += 1
        if i > 1:
            break

    if i == 0:
        await event.edit(LANG['NOT_FOUND_PLUGIN'])
    else:
        await event.edit(LANG['PLUG_DELETED'])
        time.sleep(2) 
        await event.edit(LANGG['RESTARTING'])
        try: 
            if BOTLOG:
                await event.client.send_message(BOTLOG_CHATID, "#OTORESTART \n"
                                        "Plugin silme sonrası bot yeniden başlatıldı.")

            await bot.disconnect()
        except:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)


@register(incoming=True, from_users=ASISTAN, pattern="^.premove ?(.*)")
async def asistanpremove(ups):
    """ premove komutunu asistana söylerseniz sizin yerinize plugin siler. """
    modul = ups.pattern_match.group(1).lower()
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            usp = await ups.reply(LANG['PREMOVE_DELETING'])
            i = 0
            a = 0
            async for message in event.client.iter_messages(PLUGIN_CHANNEL_ID, filter=InputMessagesFilterDocument, search=modul):
                await message.delete()
                try:
                    os.remove(f"./userbot/modules/{message.file.name}")
                except FileNotFoundError:
                    await usp.edit(LANG['ALREADY_DELETED'])

                i += 1
                if i > 1:
                    break

                if i == 0:
                    await usp.edit(LANG['NOT_FOUND_PLUGIN'])
                else:
                    await usp.edit(LANG['PLUG_DELETED'])
                    time.sleep(2) 
                    await usp.edit(LANGG['RESTARTING'])
                    try: 
                        if BOTLOG:
                            await ups.client.send_message(BOTLOG_CHATID, "#OTORESTART \n"
                                                    "Plugin silme sonrası bot yeniden başlatıldı.")

                        await bot.disconnect()
                    except:
                        pass
                    os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            return
    else:
        return


@register(incoming=True, from_users=ASISTAN, pattern="^.pinstall")
async def pinsasistan(ups):
    reply_message = None
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            reply_message = await ups.get_reply_message()
        else:
            return
    else:
        return
    usp = await ups.reply(LANG["DOWNLOADING"])
    edizin = f"./userbot/modules/{reply_message.file.name}"

    if os.path.exists(edizin):
        await usp.edit(LANG["ALREADY_INSTALLED"])
        return

    dosya = await ups.client.download_media(reply_message, "./userbot/modules/")

    try:
        spec = importlib.util.spec_from_file_location(dosya, dosya)
        mod = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(mod)
    except Exception as e:
        await usp.edit(f"{LANG['PLUGIN_BUGGED']} {e}`")
        return os.remove("./userbot/modules/" + dosya)

    dosy = open(dosya, "r").read()
    if re.search(r"@tgbot\.on\(.*pattern=(r|)\".*\".*\)", dosy):
        komu = re.findall(r"\(.*pattern=(r|)\"(.*)\".*\)", dosy)
        komutlar = ""
        i = 0
        while i < len(komu):
            komut = komu[i][1]
            CMD_HELP["tgbot_" + komut] = f"{LANG['PLUGIN_DESC']} {komut}"
            komutlar += komut + " "
            i += 1
        await usp.edit(LANG['PLUGIN_DOWNLOADED'] % komutlar)
    else:
        Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", dosy)

        if (not type(Pattern) == list) or (len(Pattern) < 1 or len(Pattern[0]) < 1):
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                return await usp.edit(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımını Öğrenmek İçin__ `.siri {cmdhelp}` __yazın.__')
            else:
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                userbot.cmdhelp.CmdHelp(dosya).add_warning('Komutlar bulunamadı!').add()
                return await usp.edit(LANG['PLUGIN_DESCLESS'])
        else:
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                return await usp.edit(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımını Öğrenmek İçin__ `.siri {cmdhelp}` __yazın.__')
            else:
                dosyaAdi = reply_message.file.name.replace('.py', '')
                extractCommands(dosya)
                await reply_message.forward_to(PLUGIN_CHANNEL_ID)
                return await usp.edit(f'**Modül Başarıyla Yüklendi**\n__Modülün  Kullanımını Öğrenmek İçin__ `.siri {dosyaAdi}` __yazın.__')



