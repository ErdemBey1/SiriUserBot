# ERDEM - BEY - SİRİ - USERBOT

import asyncio
from userbot.events import register
import os
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.video (.*)")
async def inf(event):
  try:
    await e.edit("`Siri Videoyu Ayarlıyor. Bekleyin`")
  except:
    pass
  os.system("pip install pytube")
  from pytube import YouTube
  url = event.pattern_match.group(1)
  am = YouTube(f"{url}")
  ad = am.title
  await event.edit(f"`{ad}` Siri Yüklüyor. Bekleyin...")
  yarak = YouTube(f"{url}").streams.get_highest_resolution().download()
  await event.client.send_file(event.chat_id, yarak)
  await event.delete()
  os.remove(yarak)
@register(outgoing=True, pattern="^.audio (.*)")
async def audio(e):
  try:
    await e.edit("`Siri Müzik Şekline Getiriyor. Bekleyin`")
  except:
    pass
  os.system("pip install pytube")
  from pytube import YouTube
  os.system("pip install moviepy")
  import moviepy.editor as mp
  cuk = e.pattern_match.group(1)
  am1 = YouTube(f"{cuk}")
  videoad = am1.title
  await e.edit(f"`{videoad}` yükleniyor...")
  yar = YouTube(f"{cuk}").streams.filter(file_extension='mp4').first().download()
  await e.edit(f"`{videoad}` Siri müzik olarak Ayarlıyor..")
  name = am1.title + ".mp3"
  my_clip = mp.VideoFileClip(yar)
  my_clip.audio.write_audiofile(name)
  await e.edit("`Siri Gönderiyor`")
  await e.client.send_file(e.chat_id, name)
  os.remove(yar)
  os.remove(name)
  my_clip.close()
  await e.delete()
  
  CmdHelp('ytscarp').add_command(
    'video', '.video <videolinki>', 'YouTubeden Videoları İndirirmek İçin Kullanılır'
).add_command(
    'audio', '.audio <videolinki>', 'YouTubeden Videoları Ses Dosyası Şeklinde İndirir'
).add()
