import os
import time
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@prediksibola968"

if not BOT_TOKEN:
    print("BOT_TOKEN belum diset")
    exit(1)

bot = Bot(token=BOT_TOKEN)

def kirim_jadwal():
    try:
        url = "https://www.scorebat.com/video-api/v3/"
        r = requests.get(url, timeout=15)
        data = r.json()

        pesan = "⚽ JADWAL PERTANDINGAN BOLA ⚽\n\n"

        for m in data.get("response", [])[:10]:
            pesan += f"🏆 {m.get('competition','-')}\n"
            pesan += f"⚔️ {m.get('title','-')}\n"
            pesan += f"🕒 {m.get('date','-')}\n\n"

        bot.send_message(chat_id=CHANNEL, text=pesan)
        print("Jadwal terkirim")

    except Exception as e:
        print("Error:", e)

print("Bot aktif...")

while True:
    kirim_jadwal()
    time.sleep(3600)  # 1 jam
