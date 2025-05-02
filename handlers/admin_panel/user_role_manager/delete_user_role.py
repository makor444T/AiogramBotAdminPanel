from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config.bot_config import bot
from db_handlers.user_role.check_user_role import check_user_role
from db_handlers.user_role.delete_user_role import delete_user_role
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

router = Router()


class FSM_delete_role_from_user(StatesGroup):
    user_id = State()


@router.callback_query(F.data == "delete_role_from_user")
async def admin_panel_delete_role_from_user(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(FSM_delete_role_from_user.user_id)
    await callback.message.edit_text("Введіть ID користувача", reply_markup=admin_panel_keyboard_back_to_main_menu)


@router.message(FSM_delete_role_from_user.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    try:
        int_user_id = int(message.text)
        check = await check_user_role(user_id=int_user_id)

        if check == 'None':
            await state.clear()
            await bot.send_message(
                message.chat.id,
                "Такого користувача не існує! Спробуйте ще раз.",
                reply_markup=admin_panel_keyboard_back_to_main_menu
            )
            return
        else:
            await delete_user_role(user_id=int_user_id)
            await state.clear()
            await bot.send_message(
                message.chat.id,
                f"Роль користувача з ID: {int_user_id} видалена",
                reply_markup=admin_panel_keyboard_back_to_main_menu
            )

    except ValueError:
        await state.clear()
        await bot.send_message(
            message.chat.id,
            "ID користувача має бути числом. Спробуйте ще раз.",
            reply_markup=admin_panel_keyboard_back_to_main_menu
        )
