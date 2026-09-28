import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "TELEGRAM_BOT_TOKEN"
VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Start komandasi
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("🛡 Salom! Men kibеr himoya botiman.\n"
                    "Menga link yuboring, tekshirib beraman.\n"
                    "Komandalar: /help /advice")


# Help komandasi
@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await msg.reply("📌 Komandalar:\n"
                    "/start - Botni ishga tushirish\n"
                    "/help - Yordam\n"
                    "/advice - Xavfsizlik bo‘yicha maslahatlar\n"
                    "Link yuboring - xavfsizlik tekshiruvi")


# Maslahat komandasi
@dp.message_handler(commands=['advice'])
async def advice_cmd(msg: types.Message):
    tips = [
        "Hech qachon noma’lum linkni bosmang.",
        "Parollaringizni muntazam yangilang.",
        "Ikki bosqichli autentifikatsiyani yoqing.",
        "Antivirusni yangilab turing."
    ]
    await msg.reply("🔒 Xavfsizlik bo‘yicha maslahatlar:\n- " + "\n- ".join(tips))


# Link tekshiruv
@dp.message_handler()
async def check(msg: types.Message):
    url = msg.text.strip()
    if url.startswith("http"):
        try:
            headers = {"x-apikey": VT_API_KEY}
            response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url}", headers=headers)

            if response.status_code == 200:
                data = response.json()
                stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
                malicious = stats.get("malicious", 0)
                suspicious = stats.get("suspicious", 0)

                if malicious > 0 or suspicious > 0:
                    await msg.reply(
                        f"⚠️ Link xavfli bo‘lishi mumkin!\nMalicious: {malicious}, Suspicious: {suspicious}")
                else:
                    await msg.reply("✅ Link xavfsiz ko‘rinmoqda.")
            else:
                await msg.reply("❌ Tekshiruvda xatolik yuz berdi.")
        except Exception as e:
            await msg.reply(f"❌ Xatolik: {e}")
    else:
        await msg.reply("❗ Iltimos, to‘liq link yuboring (http:// yoki https:// bilan).")


if name == "main":
    executor.start_polling(dp, skip_updates=True)import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "TELEGRAM_BOT_TOKEN"
VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("🛡 Salom! Men kibеr himoya botiman.\n"
                    "Menga link yuboring, tekshirib beraman.\n"
                    "Komandalar: /help /advice")

# Help komandasi
@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await msg.reply("📌 Komandalar:\n"
                    "/start - Botni ishga tushirish\n"
                    "/help - Yordam\n"
                    "/advice - Xavfsizlik bo‘yicha maslahatlar\n"
                    "Link yuboring - xavfsizlik tekshiruvi")

# Maslahat komandasi
@dp.message_handler(commands=['advice'])
async def advice_cmd(msg: types.Message):
    tips = [
        "Hech qachon noma’lum linkni bosmang.",
        "Parollaringizni muntazam yangilang.",
        "Ikki bosqichli autentifikatsiyani yoqing.",
        "Antivirusni yangilab turing."
    ]
    await msg.reply("🔒 Xavfsizlik bo‘yicha maslahatlar:\n- " + "\n- ".join(tips))

# Link tekshiruv
@dp.message_handler()
async def check(msg: types.Message):
    url = msg.text.strip()
    if url.startswith("http"):
        try:
            headers = {"x-apikey": VT_API_KEY}
            response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url}", headers=headers)

            if response.status_code == 200:
                data = response.json()
                stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
                malicious = stats.get("malicious", 0)
                suspicious = stats.get("suspicious", 0)

                if malicious > 0 or suspicious > 0:
                    await msg.reply(f"⚠️ Link xavfli bo‘lishi mumkin!\nMalicious: {malicious}, Suspicious: {suspicious}")
                else:
                    await msg.reply("✅ Link xavfsiz ko‘rinmoqda.")
            else:
                await msg.reply("❌ Tekshiruvda xatolik yuz berdi.")
        except Exception as e:
            await msg.reply(f"❌ Xatolik: {e}")
    else:
        await msg.reply("❗ Iltimos, to‘liq link yuboring (http:// yoki https:// bilan).")

if name == "main":
    executor.start_polling(dp, skip_updates=True)