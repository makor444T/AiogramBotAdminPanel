import asyncio

from config.bot_config import bot, dp
from handlers.admin_panel import main_menu
from handlers.admin_panel.post_manager import create_post, delete_post
from handlers.admin_panel.user_role_manager import create_user_role, delete_user_role
from handlers.admin_panel.user_roles.base_user_role_fsm import router as user_role_router
from handlers.admin_panel.user_roles.role_callbacks import router as callback_router
from handlers.start import router as start_router

routers = [
    create_post.router,
    delete_post.router,
    main_menu.router,
    start_router,
    create_user_role.router,
    delete_user_role.router,
    callback_router,
    user_role_router,
]


async def main():
    dp.include_routers(*routers)
    await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
