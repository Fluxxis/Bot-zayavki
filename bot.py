import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --------------------
# НАСТРОЙКИ (впиши свои)
# --------------------
BOT_TOKEN = "7995968509:AAFBjVY8_Sq4qqFYzYpT9E2BodUdUlj-XGM"
WEBAPP_URL = "https://zayavki-lilac.vercel.app"  # ссылка на web-app (HTTPS)

START_TEXT = "Хочешь быть тем самый, тем самым который смог?\nТак спеши!👇"


async def on_start(message: Message) -> None:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть Web-App",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )
    await message.answer(START_TEXT, reply_markup=kb)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    if not BOT_TOKEN or BOT_TOKEN == "PUT_YOUR_BOT_TOKEN_HERE":
        raise SystemExit("В bot.py вставь BOT_TOKEN.")

    if not WEBAPP_URL.startswith("https://"):
        raise SystemExit("WEBAPP_URL должен начинаться с https://")

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(on_start, CommandStart())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
