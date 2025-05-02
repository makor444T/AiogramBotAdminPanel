from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel_keyboard_take_user_role = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Адміністратор', callback_data='role_admin'),
            InlineKeyboardButton(text='Контент-менеджер', callback_data='role_content_manager')
        ]
    ]
)
