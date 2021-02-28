# Copyright (C) 2020 Yusuf Usta.
#
# Licensed under the  GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# SiriUserBot - ErdemBey - Midy

import os
from telethon.tl.types import InputMessagesFilterDocument
from userbot.events import register
from userbot import BOT_USERNAME, PATTERNS, CMD_HELP, PLUGIN_CHANNEL_ID
import userbot.cmdhelp
from random import choice, sample
import importlib
import re
from userbot.main import extractCommands

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__plugin")

# ████████████████████████████████ #

# Plugin Mağazası
@register(outgoing=True, pattern="^.store ?(.*)")
@register(outgoing=True, pattern="^.ma[gğ]aza ?(.*)")
async def magaza(event):
    plugin = event.pattern_match.group(1)
    await event.edit('** Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n`🔎 Plugin\'i Getiriyorum, Lütfen Bekle!`')
    split = plugin.split()
    if plugin == '':
        plugin = 'Son Yüklenen'
        plugins = await event.client.get_messages('@siriplugin', limit=15, filter=InputMessagesFilterDocument)
    elif len(split) >= 1 and (split[0] == 'random' or split[0] == 'rastgele'):
        plugin = 'Rastgele'
        plugins = await event.client.get_messages('@siriplugin', limit=None, filter=InputMessagesFilterDocument)
        plugins = sample(plugins, int(split[1]) if len(split) == 2 else 5)
    else:
        plugins = await event.client.get_messages('@siriplugin', limit=None, search=plugin, filter=InputMessagesFilterDocument)
        random = await event.client.get_messages('@siriplugin', limit=None, filter=InputMessagesFilterDocument)
        random = choice(random)
        random_file = random.file.name

    result = f'** Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n**🔎 Veriler:** `{plugin}`\n**🔢 Sonuç: __({len(plugins)})__**\n➖➖➖➖➖\n\n'
    
    if len(plugins) == 0:
        result += f'**Bu İsimde Plugin Bulamadım...**\n`{random_file}` __Bu plugini Denemek İster Misin ?__'
    else:
        for plugin in plugins:
            plugin_lines = plugin.raw_text.splitlines()
            result += f'**⬇️ {plugin_lines[0]}** `({plugin.file.name})`**:** '
            if len(plugin_lines[2]) < 50:
                result += f'__{plugin_lines[2]}__'
            else:
                result += f'__{plugin_lines[2][:50]}...__'
            result += f'\n**ℹ️ Yüklemek için:** `{PATTERNS[:1]}sinstall {plugin.id}`\n➖➖➖➖➖\n'
    return await event.edit(result)

# Plugin Mağazası
@register(outgoing=True, pattern="^.sy[üu]kle ?(.*)")
@register(outgoing=True, pattern="^.sinstall ?(.*)")
async def sinstall(event):
    plugin = event.pattern_match.group(1)
    try:
        plugin = int(plugin)
    except:
        return await event.edit('**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n**⚠️ Hata:** `Lütfen Sadece Say Yazınız .sinstall pluginid`')
    
    await event.edit('**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n`🔎 Plugin\'i Getiriyorum...`')
    plugin = await event.client.get_messages('@siriplugin', ids=plugin)
    await event.edit(f'**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n`✅ {plugin.file.name} Plugini Getirildi!`\n`⬇️ Plugini Yüklüyorum... Bekleyin.`')
    dosya = await plugin.download_media('./userbot/modules/')
    await event.edit(f'**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n`✅ {plugin.file.name} indirme başarılı!`\n`⬇️ Plugini Yüklüyorum... Bekleyin.`')
    
    try:
        spec = importlib.util.spec_from_file_location(dosya, dosya)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as e:
        os.remove("./userbot/modules/" + dosya)
        return await event.edit(f'**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n**⚠️ Hata:** `Plugin Hatalı. {e}`\n**LÜTFEN BUNU ADMİNLERE BİLDİRİN!**')

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
                await plugin.forward_to(PLUGIN_CHANNEL_ID)
                return await event.edit(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımı İçin__ `.siri {cmdhelp}` __Yazın.__')
            else:
                await plugin.forward_to(PLUGIN_CHANNEL_ID)
                userbot.cmdhelp.CmdHelp(dosya).add_warning('Komutlar bulunamadı!').add()
                return await event.edit(LANG['PLUGIN_DESCLESS'])
        else:
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await plugin.forward_to(PLUGIN_CHANNEL_ID)
                return await event.edit(f'**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n**✅ Modül Başarıyla Yüklendi!**\n__ℹ️ Modülün Kullanımını Öğrenmek İçin__ `.siri {cmdhelp}` __Yazınız.__')
            else:
                dosyaAdi = plugin.file.name.replace('.py', '')
                extractCommands(dosya)
                await plugin.forward_to(PLUGIN_CHANNEL_ID)
                return await event.edit(f'**Siri Plugin Mağazası**\n__Versiyon 1.0__\n\n**✅ Modül Başarıyla Yüklendi!**\n__ℹ️ Modülün Kullanımını Öğrenmek İçin__ `.siri {dosyaAdi}` __Yazınız.__')

userbot.cmdhelp.CmdHelp('store').add_command(
    'store', '<kelime>', 'Plugin kanalına son atılan Pluginleri getirir. Eğer kelime yazarsanız onu kanalda arar.'
).add_command(
    'store random', '<say>', 'Plugin kanalından random plugin getirir.', 'store random 10'
).add_command(
    'sinstall', '<say>', 'Plugin kanalından direkt olarak Plugini yükler.'
).add()
