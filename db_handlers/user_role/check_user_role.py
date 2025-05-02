import asyncpg

from config.bot_config import HOST, PASSWORD, USER, DB


async def check_user_role(user_id):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)
    user_role = await conn.fetch("SELECT user_role FROM users WHERE user_id = $1", user_id)
    await conn.close()

    if not user_role:
        return None
    else:
        return user_role[0]['user_role']
