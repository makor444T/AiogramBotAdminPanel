from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from handlers.admin_panel.user_roles.base_user_role_fsm import start_user_role_creation

router = Router()


@router.callback_query(F.data == "role_admin")
async def create_admin_callback(callback: types.CallbackQuery, state: FSMContext):
    await start_user_role_creation(callback, state, role="admin")


@router.callback_query(F.data == "role_content_manager")
async def create_cm_callback(callback: types.CallbackQuery, state: FSMContext):
    await start_user_role_creation(callback, state, role="content_manager")
