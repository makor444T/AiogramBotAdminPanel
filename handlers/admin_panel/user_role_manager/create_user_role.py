from aiogram import types, Router, F

from keyboards.admin_panel_keyboard_take_user_role import admin_panel_keyboard_take_user_role

router = Router()


@router.callback_query(F.data == "make_user_role")
async def admin_panel_create_user_role(callback: types.CallbackQuery):
    await callback.message.edit_text("Оберіть роль", reply_markup=admin_panel_keyboard_take_user_role)
