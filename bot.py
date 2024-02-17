import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from config import TOKEN
from keyboards import create_inline_kb, create_inline_kb_start_lesson, create_inline_kb_lesson
from database import dbase

topics = ['perfekt', 'verb', 'adjective', 'noun', 'adverb']

# dbase = Database()


class FSMChooseTopic(StatesGroup):
    perfekt_task = State()
    perfekt_answer = State()


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
    await call.message.answer(text='User get a bunch of lessons',
                              reply_markup=create_inline_kb_start_lesson())
    await state.set_state(FSMChooseTopic.perfekt_task)

    await call.answer()


@dp.message(FSMChooseTopic.perfekt_task)
@dp.callback_query(F.data == 'get_task')
async def perfekt_2(call: CallbackQuery, state: FSMContext):
    task, correct_answer = dbase.get_random_task('perfekt')
    await state.update_data(correct_answer=correct_answer)
    await call.message.answer(text=task)
    await state.set_state(FSMChooseTopic.perfekt_answer)

    await call.answer()


@dp.message(FSMChooseTopic.perfekt_task)
@dp.callback_query(F.data == 'stop_lesson')
async def perfekt_2(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text='Вы завершили урок')
    await state.clear()

    await call.answer()


@dp.message(FSMChooseTopic.perfekt_answer)
async def perfekt(message: Message, state: FSMContext):
    await state.update_data(user_answer=message.text)
    user_data = await state.get_data()
    correct_answer = user_data['correct_answer']
    user_answer = user_data['user_answer']
    if user_answer == correct_answer:
        await message.answer(text=f'✅ Вы ответили правильно:\n\n{correct_answer}',
                             reply_markup=create_inline_kb_lesson())
    else:
        await message.answer(text=f'❌ Вы ошиблись, правильный ответ:\n\n{correct_answer}',
                             reply_markup=create_inline_kb_lesson())
    await state.set_data({})
    await state.set_state(FSMChooseTopic.perfekt_task)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
