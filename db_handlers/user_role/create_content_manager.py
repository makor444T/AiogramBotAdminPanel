import asyncpg

from config.bot_config import USER, PASSWORD, DB, HOST


async def create_content_manager(user_id: int, user_name: str):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)
    await conn.execute("INSERT INTO users (user_id, user_name, user_role) VALUES ($1, $2, $3)", user_id, user_name,
                       'content_manager')
    await conn.close()
