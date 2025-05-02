import asyncpg

from config.bot_config import USER, PASSWORD, DB, HOST


async def delete_post(post_id: int):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)
    try:
        result = await conn.execute("DELETE FROM posts WHERE id = $1", post_id)
        return result.endswith("1")
    finally:
        await conn.close()
