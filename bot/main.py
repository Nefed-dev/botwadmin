from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery, InputMediaPhoto, InputFile

from keyboard import KeyboardMaker

from base import get_session
from crud import Crud
from settings import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def hello_message(message: types.Message):
    s = await get_session()
    message_ = await Crud(session=s).get_one(id=0)
    data = await Crud(session=s).get_by_parent_id(parent_id=0)
    kbs = KeyboardMaker.make_kb(parent=message_, data=data)
    await message.answer(text=message_.message_text, reply_markup=kbs)


@dp.callback_query_handler(text_contains="msg_")
async def exercise_keyboard(query: CallbackQuery):
    msg_id = int(query.data.split("_")[1])
    s = await get_session()
    parent = await Crud(session=s).get_one(id=msg_id)
    data = await Crud(session=s).get_by_parent_id(parent_id=msg_id)
    kbs = KeyboardMaker.make_kb(parent=parent, data=data)
    chat_id = query.from_user.id
    if parent.media:
        for media in parent.media:
            await bot.send_photo(chat_id=chat_id, photo=media)
    await query.message.answer(text=parent.message_text, reply_markup=kbs)


if __name__ == "__main__":
    print("start")
    executor.start_polling(dispatcher=dp)
