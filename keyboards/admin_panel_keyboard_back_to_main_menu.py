from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel_keyboard_back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Головне меню', callback_data='main_menu')]
    ]
)
