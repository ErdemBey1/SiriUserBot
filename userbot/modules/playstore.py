# SiriUserBot - ErdemBey - Berceste - Midy

import bs4
import requests

from userbot.events import register

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("playstore")

# ████████████████████████████████ #

@register(outgoing=True, pattern=".playstore ?(.*)")
async def play_store(message):
    try:
        await message.edit(LANG["SEARCH"])
        app_name = message.pattern_match.group(1)
        if len(app_name) < 1:
            await message.edit(f'`{LANG["EKS"]} : ``.playstore Telegram`')
            return
            
        remove_siri = app_name.split(' ')
        final_name = '+'.join(remove_siri)
        page = requests.get(f"https://play.google.com/store/search?q={final_name}&c=apps")
        soup = bs4.BeautifulSoup(page.content, 'lxml', from_encoding='utf-8')
        results = soup.findAll("div", "ZmHEEd")
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext(
            'div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += f'\n\n<code>{LANG["SAHP"]}</code> <a href='" + app_dev_link + "'>'
        app_details += app_dev + "</a>"
        app_details += f'\n<code>{LANG["PUAN"]}</code> ' + app_rating.replace(
            "Rated ", "").replace(" out of ", "/").replace(
                " stars", "", 1).replace(" stars", "⭐️").replace("five", "5")
        app_details += f"\n<code>{LANG['OZLLK']}</code> <a href='" + app_link + "'>Google Play'da göster</a>"
        await message.edit(app_details, parse_mode='html')
    except IndexError:
        await message.edit(LANG["NOT_FOUND"])
