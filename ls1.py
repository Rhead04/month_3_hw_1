from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
from decouple import config

Token = config("TOKEN")

bot = Bot(Token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Hello my friend {message.from_user.full_name}")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup=InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько цветов радуге?"
    answer = ['12', '6', '7', '8']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Каждый Охотник Желатет Знать Где Сидит Фазан",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call:types.CallbackQuery):
    markup=InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Какой по счету месяц идет наш курс?"
    answer = ['1', '2', '3', '4']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Каждый Охотник Желатет Знать Где Сидит Фазан",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):

    photo = open("media/ctrl c.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)



@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, int(message.text) ** 2)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)