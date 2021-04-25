# SiriUserBot •_• # Erdem - Berceste

from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot.events import register

#Siri Yapıyor Bişiler

@register(outgoing=True, pattern="^.yap (1|2|3)(?: |$)(.*)")

async def telegraphs(grup):

    """ .yap command,Sipariş Alındı Siri Yapmaya Başladı... :)  """

    if not grup.text[0].isalpha() and grup.text[0] not in ("/", "#", "@", "!"):

        if grup.fwd_from:

            return

        type_of_group = grup.pattern_match.group(1)

        group_name = grup.pattern_match.group(2)

        if type_of_group == "1":

            try:

                result = await grup.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602

                    users=["@muinrobot"],

                    title=group_name

                ))

                created_chat_id = result.chats[0].id

                await grup.client(functions.messages.DeleteChatUserRequest(

                    chat_id=created_chat_id,

                    user_id="@muinrobot"

                ))

                result = await grup.client(functions.messages.ExportChatInviteRequest(

                    peer=created_chat_id,

                ))

                await grup.edit("`{}` Siparişinizi Hazırladım, Sahip. \nGörmek için: [{}]({})".format(group_name, group_name, result.link))

            except Exception as e:  # pylint:disable=C0103,W0703

                await grup.edit(str(e))

        elif type_of_group == "1" or type_of_group == "2":

            try:

                r = await grup.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602

                    title=group_name,

                    about="SiriUserbot Tarafından Yapılmıştır",

                    megagroup=False if type_of_group == "3" else True

                ))

                created_chat_id = r.chats[0].id

                result = await grup.client(functions.messages.ExportChatInviteRequest(

                    peer=created_chat_id,

                ))

                await grup.edit("`{}` Siparişinizi Hazırladım, Sahip. \nGörmek için: [{}]({})".format(group_name, group_name, result.link))

            except Exception as e:  # pylint:disable=C0103,W0703

                await grup.edit(str(e))



CMD_HELP.update({

    "yap": "\
Yap\
\nKullanımı: Süper/gizli Grup, kanal Hazırlar.\
\n\n`.yap 1 <ad>`\
\nKullanımı: Gizli Grup Hazırlar.\
\n\n`.yap 2 <ad>`\
\nKullanımı: Herkese açık Grup Hazırlar.\
\n\n`.yap 3 <ad>`\
\nKullanımı: Kanal Hazırlar.\
"})
