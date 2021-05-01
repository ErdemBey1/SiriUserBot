# ÜÇ YAZILIMCI BİNDİK BİR GEMİYE GİDİYORUZ İLERİYE
FROM siriuserbot/siriuserbot:latest
RUN git clone https://github.com/ErdemBey1/SiriUserBot /root/SiriUserBot
WORKDIR /root/SiriUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
