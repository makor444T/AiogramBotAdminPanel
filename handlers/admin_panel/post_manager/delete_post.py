from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from db_handlers.post_manager.delete_post import delete_post
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu

router = Router()


class FSM_delete_post(StatesGroup):
    post_id = State()


@router.callback_query(F.data == "delete_post")
async def admin_panel_delete_post(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(FSM_delete_post.post_id)
    await callback.message.edit_text("Введіть ID поста для видалення", reply_markup=admin_panel_keyboard_main_menu)


@router.message(FSM_delete_post.post_id)
async def load_post_id(message: types.Message, state: FSMContext):
    try:
        post_id = int(message.text)
        result = await delete_post(post_id=post_id)

        if result:
            await state.clear()
            await message.answer(f"Пост з ID {post_id} успішно видалено.", reply_markup=admin_panel_keyboard_main_menu)
        else:
            await state.clear()
            await message.answer(f"Пост з ID {post_id} не знайдено або не вдалося видалити.",
                                 reply_markup=admin_panel_keyboard_main_menu)

    except ValueError:
        await state.clear()
        await message.answer("ID поста має бути числом. Спробуйте ще раз.", reply_markup=admin_panel_keyboard_main_menu)
