import asyncio
import ollama

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8850831355:AAHN-q3HZlJbDeuTU56ArilchY1_SuCUKy8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤖 Savol berish"),
         KeyboardButton(text="📚 Ma'lumot")],
        [KeyboardButton(text="📞 Bog'lanish"),
         KeyboardButton(text="ℹ️ Bot haqida")],
        [KeyboardButton(text="⚙️ Sozlamalar")]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Assalomu alaykum! 👋\n"
        "Men N=1 botman 🤖\n\n"
        "Menga istalgan savolingizni yozing.",
        reply_markup=keyboard
    )


@dp.message()
async def answer(message: types.Message):

    text = message.text

    if text == "🤖 Savol berish":
        await message.answer("Savolingizni yozing 👇")
        return

    if text == "📚 Ma'lumot":
        await message.answer(
            "Men turli mavzularda ma'lumot berishga harakat qilaman. 📚\n"
            "Savolingizni yozing."
        )
        return

    if text == "📞 Bog'lanish":
        await message.answer("Bog'lanish uchun boshliq: @Bahadirvna_a7")
        return

    if text == "ℹ️ Bot haqida":
        await message.answer(
            "Bu Telegram AI yordamchi bot. 🤖\n"
            "Javoblarni 7-osmondan oladi."
        )
        return

    if text == "⚙️ Sozlamalar":
        await message.answer("Sozlamalar hozircha ishlab chiqilmoqda ⚙️")
        return

    try:
        result = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": "Sen o'zbek tilida javob beradigan yordamchi botsan. Javoblarni oddiy va tushunarli yoz."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        javob = result["message"]["content"]

        await message.answer(javob)

    except Exception as e:
        await message.answer(
            "❌ Xatolik yuz berdi.Savolingiz noaniq\n"
            "Ollama ishlayotganini tekshiring."
        )

        print("XATOLIK:", e)


async def main():
    print("🤖 Bot ishlayapti...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())