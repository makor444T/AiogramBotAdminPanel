import datetime

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config.bot_config import CHAT_ID
from db_handlers.post_manager.create_post import create_post
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

router = Router()


class FSM_create_post(StatesGroup):
    post_name = State()
    post_description = State()
    post_image = State()
    post_tag = State()


@router.callback_query(F.data == "post_manager")
async def create_post_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(FSM_create_post.post_name)
    await callback.message.edit_text("Введіть назву поста", reply_markup=admin_panel_keyboard_back_to_main_menu)


@router.message(FSM_create_post.post_name)
async def process_post_name(message: types.Message, state: FSMContext):
    if not message.text.strip():
        await message.answer("Назва поста не може бути порожньою. Будь ласка, введіть назву.")
        return
    await state.update_data(post_name=message.text)
    await state.set_state(FSM_create_post.post_description)
    await message.answer("Введіть опис поста", reply_markup=admin_panel_keyboard_back_to_main_menu)


@router.message(FSM_create_post.post_description)
async def process_post_description(message: types.Message, state: FSMContext):
    if not message.text.strip():
        await message.answer("Опис поста не може бути порожнім. Будь ласка, введіть опис.")
        return
    await state.update_data(post_description=message.text)
    await state.set_state(FSM_create_post.post_image)
    await message.answer("Надішліть зображення", reply_markup=admin_panel_keyboard_back_to_main_menu)


@router.message(F.photo, FSM_create_post.post_image)
async def process_post_image(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Будь ласка, надішліть зображення.")
        return
    photo_id = message.photo[-1].file_id
    await state.update_data(post_image=photo_id)
    await state.set_state(FSM_create_post.post_tag)
    await message.answer("Введіть теги (через кому). Приклад: #тег1, #тег2",
                         reply_markup=admin_panel_keyboard_back_to_main_menu)


@router.message(FSM_create_post.post_tag)
async def process_post_tag(message: types.Message, state: FSMContext):
    tags = message.text.strip()
    if not tags:
        await message.answer("Теги не можуть бути порожніми. Будь ласка, введіть хоча б один тег.")
        return
    await state.update_data(post_tag=tags)
    data = await state.get_data()

    now = datetime.datetime.now()
    await create_post(
        post_name=data['post_name'],
        post_description=data['post_description'],
        post_image=data['post_image'],
        post_tag=data['post_tag'],
        user_name=message.from_user.full_name,
        create_date=now.strftime("%Y-%m-%d"),
        create_time=now.strftime("%H:%M:%S"),
    )

    caption = (
        f"<b>{data['post_name']}</b>\n\n"
        f"{data['post_description']}\n\n"
        f"<i>Теги:</i> {data['post_tag']}"
    )

    await message.bot.send_photo(chat_id=CHAT_ID, photo=data['post_image'], caption=caption, parse_mode="HTML")

    post_info = (
        f"<b>Назва поста:</b> {data['post_name']}\n"
        f"<b>Опис:</b> {data['post_description']}\n"
        f"<b>Теги:</b> {data['post_tag']}\n"
        f"<b>Дата:</b> {now.strftime('%Y-%m-%d')}\n"
        f"<b>Час:</b> {now.strftime('%H:%M:%S')}"
    )

    await message.bot.send_photo(
        chat_id=message.chat.id,
        photo=data['post_image'],
        caption=post_info,
        parse_mode="HTML"
    )

    await message.answer("Пост успішно створено!")
    await state.clear()
