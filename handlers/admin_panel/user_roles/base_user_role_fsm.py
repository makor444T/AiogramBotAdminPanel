from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config.bot_config import bot
from db_handlers.user_role.create_admin import create_admin
from db_handlers.user_role.create_content_manager import create_content_manager
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


class FSM_create_user_role(StatesGroup):
    user_id = State()
    user_name = State()


async def start_user_role_creation(callback: types.CallbackQuery, state: FSMContext, role: str):
    await state.set_state(FSM_create_user_role.user_id)
    await state.update_data(role=role)
    await callback.message.edit_text("Введіть ID користувача", reply_markup=admin_panel_keyboard_back_to_main_menu)


role_creators = {
    "admin": create_admin,
    "content_manager": create_content_manager,
}

from db_handlers.user_role.check_user_role import check_user_role

router = Router()


@router.message(FSM_create_user_role.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        if user_id < 0:
            raise ValueError("ID не може бути від'ємним")

        existing_role = await check_user_role(user_id=user_id)
        if existing_role:
            await state.clear()
            await bot.send_message(
                message.chat.id,
                f"Цей користувач вже має роль {existing_role.replace('_', ' ')}!",
                reply_markup=admin_panel_keyboard_back_to_main_menu
            )
        else:
            await state.update_data(user_id=user_id)
            await state.set_state(FSM_create_user_role.user_name)
            await bot.send_message(
                message.chat.id,
                f"ID: {user_id} прийнято.\nВведіть ім'я користувача:",
                reply_markup=admin_panel_keyboard_back_to_main_menu
            )
    except ValueError:
        await bot.send_message(
            message.chat.id,
            "ID має бути позитивним числом. Спробуйте ще раз.",
            reply_markup=admin_panel_keyboard_back_to_main_menu
        )


@router.message(FSM_create_user_role.user_name)
async def load_user_name(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.clear()
        await bot.send_message(
            message.chat.id,
            "Ім'я користувача не повинно бути числом. Спробуйте ще раз.",
            reply_markup=admin_panel_keyboard_back_to_main_menu
        )
        return

    data = await state.get_data()
    create_func = role_creators.get(data['role'])

    if not create_func:
        await state.clear()
        await bot.send_message(message.chat.id, "Помилка: невідома роль.")
        return

    await create_func(user_id=data['user_id'], user_name=message.text)
    await state.clear()
    await bot.send_message(
        message.chat.id,
        f"Роль «{data['role'].replace('_', ' ')}» призначена користувачу з ID {data['user_id']}.",
        reply_markup=admin_panel_keyboard_back_to_main_menu
    )
