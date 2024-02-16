from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# Функция для формирования инлайн-клавиатуры на лету
def create_inline_kb(width: int = 3,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def create_inline_kb_start_lesson():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Übung",
        callback_data="get_task")
    )

    return builder.as_markup()


def create_inline_kb_lesson():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Stop",
            callback_data="stop_lesson"),
        InlineKeyboardButton(
            text="Weiter",
            callback_data="get_task")
    )

    return builder.as_markup()
