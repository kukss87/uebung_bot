import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from config import TOKEN
from keyboards import create_inline_kb

topics = ['perfekt', 'pronomen', 'verb', 'adjective', 'noun', 'adverb']


class FSMUsersProgress(StatesGroup):
    lesson = State()


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}!')
    await message.answer('Send me command /text')


@dp.message(Command('text'))
async def text(message: Message):
    await message.answer(text='Well done!',
                         reply_markup=create_inline_kb(2, *topics))


@dp.callback_query(F.data == 'perfekt')
async def perfekt(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text='User goes to state: FSMPerfekt')
    await call.message.answer(text='User get a bunch of lessons')
    await state.set_state(FSMUsersProgress.lesson)

    await call.answer()





async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
