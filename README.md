
----

<div align="center">
  <img src="https://github.com/ErdemBey1/SiriNewInstaller/blob/main/SiriLogo.jpg" width="300" height="300">
  <h1>Ⲋⲓⲅⲓ Ⳙ⳽ⲉⲅⲂⲟⲧ</h1>
</div>
<p align="center">
    Siri UserBot, Telegram kullanmanızı kolaylaştıran bir bottur. Tamamen açık kaynaklı ve ücretsizdir. <br>
    Siri UserBot is a bot that makes it easy to use Telegram. It is completely open source and free.
    <br>
        <a href="https://github.com/ErdemBey1/SiriUserBot/blob/master/README.md#kurulum">| Kurulum/Setup</a> |
        <a href="https://github.com/ErdemBey1/SiriUserBot/wiki/G%C3%BCncelleme">Güncelleme/Update</a> |
        <a href="https://t.me/SiriUserBot">Telegram </a> |
        <a href="https://t.me/SiriSupport">Destek/Support</a> |
    <br>
</p>

----

## Kurulum / Setup

**Android:** Termuxu açın ve bu kodu yapıştırın:

` bash <(curl -L https://bit.ly/3tUBVha) `

**iOS:**  

`apk update && apk add bash && apk add curl && curl -L -o siri_installer.sh https://bit.ly/3ayPGdk && chmod +x siri_installer.sh && bash siri_installer.sh`

**Online Kurulum**

[![Run on Repl.it](https://repl.it/badge/github/ErdemBey1/siriinstaller)](https://repl.it/@ErdemBey1/siriinstaller)

**Windows 10:** Windows 10: [Python](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab) indirin ardından PowerShell bu kodu yapıştırın:
`Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://bit.ly/3dEefrp')`

### Basit Yöntem
Eğer botu kurma hakkında fikriniz yoksa buradan Yardım Alabilirsiniz: [Kurulum Rehberi](https://t.me/sirisupport)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ErdemBey1/SiriUserBot)
### Zor Yöntem
```python
git clone https://github.com/ErdemBey1/SiriUserBot.git
cd SiriUserBot
pip install -r requirements.txt
# Config.env oluşturun ve düzenleyin. #
python3 main.py
```

## Örnek Plugin
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunu ekleyin.

@register(outgoing=True, pattern="^.deneme")
async def deneme(event):
    await event.edit('Gerçekten deneme!')

Help = CmdHelp('deneme') # Bilgi ekleyeceğiz diyoruz.
Help.add_command('deneme', # Komut
    None, # Komut parametresi varsa yazın yoksa None yazın
    'Gerçekten deneme yapıyor!', # Komut açıklaması
    'deneme' # Örnek kullanım.
    )
Help.add_info('@Erdembey1 tarafından yapılmıştır.') # Bilgi ekleyebilirsiniz.
# Ya da uyarı --> Help.add_warning('KULLANMA!')
Help.add() # Ve Ekleyelim.
```

## Bilgilendirme
Herhangi bir istek & şikâyet & öneri varsa [destek grubuna](https://t.me/SiriSupport) ulaşabilirsiniz.

```
    Userbottan dolayı; Telegram hesabınız yasaklanabilir.
    Bu bir açık kaynaklı projedir, yaptığınız her işlemden kendiniz sorumlusunuz. Kesinlikle Siri yöneticileri sorumluluk kabul etmemektedir.
    Siriyi kurarak bu sorumlulukları kabul etmiş sayılırsınız.
```
### Geliştiriciler / Developers
[![Erdem Bey](https://github.com/erdembey1.png?size=100)](https://github.com/erdembey1)  [![Midy](https://github.com/ribonney.png?size=100)](https://github.com/ribonney)  [![Berce](https://github.com/must4f.png?size=100)](https://github.com/must4f)



