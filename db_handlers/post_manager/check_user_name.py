import asyncpg

from config.bot_config import HOST, PASSWORD, USER, DB


async def check_user_name(user_id):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)
    row = await conn.fetch("SELECT user_name FROM users WHERE user_id = $1", user_id)
    await conn.close()

    if not row:
        return None
    else:
        return row[0]['user_name']
