from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN



bot = Bot(token=TOKEN)
dp = Dispatcher()
