from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import bot


# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("spaminfo")

# ████████████████████████████████ #


@register(outgoing=True, pattern=r"^.spaminfo")
async def _(event):
    await event.edit("🔄")
    chat = "@spambot"
    async with bot.conversation(chat) as conv:
        try:     
            await conv.send_message("/start")
        except YouBlockedUserError:
            await event.client(UnblockRequest(178220800))
            await conv.send_message("/start")
        spamdurumu = await conv.get_response()
        await event.delete()
        await event.client.send_read_acknowledge(conv.chat_id)
        if spamdurumu.text.startswith("Dear"):
            await event.client.forward_messages(event.chat_id, spamdurumu)
        elif spamdurumu.text.startswith("Good news"):
            await event.edit(LANG["BIRD"])
        else:
            await event.client.forward_messages(event.chat_id, spamdurumu)



dnammonc_dda = CmdHelp('spaminfo')
dnammonc_dda.add_command("spaminfo", None, "Hesabınızın spam durumunu kontrol edin").add()
