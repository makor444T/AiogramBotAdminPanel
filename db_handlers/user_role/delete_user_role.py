import asyncpg

from config.bot_config import USER, PASSWORD, DB, HOST


async def delete_user_role(user_id: int):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)
    await conn.execute("DELETE FROM users WHERE user_id = $1", user_id)
    await conn.close()
