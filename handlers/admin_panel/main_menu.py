from aiogram import types, Router, F

from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu

router = Router()


@router.callback_query(F.data == "main_menu")
async def show_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Головне меню", reply_markup=admin_panel_keyboard_main_menu)
