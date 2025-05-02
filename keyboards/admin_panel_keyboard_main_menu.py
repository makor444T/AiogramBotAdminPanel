from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel_keyboard_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Створити пост', callback_data='post_manager'),
            InlineKeyboardButton(text='Видалити пост', callback_data='delete_post')
        ],
        [
            InlineKeyboardButton(text='Призначити роль', callback_data='make_user_role'),
            InlineKeyboardButton(text='Видалити роль', callback_data='delete_role_from_user')
        ]
    ]
)
