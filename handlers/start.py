from aiogram import Router, types
from aiogram.filters import Command

from db_handlers.user_role.check_user_role import check_user_role
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    if message.chat.type != "private":
        return

    user_id = int(message.from_user.id)
    check_role = await check_user_role(user_id=user_id)

    if check_role == 'admin':
        await message.answer('Привіт, адміністратор!',
                             reply_markup=admin_panel_keyboard_main_menu)
    else:
        await message.answer('Привіт, користувач!')
