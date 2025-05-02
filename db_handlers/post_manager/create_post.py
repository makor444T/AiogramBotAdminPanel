import asyncpg

from config.bot_config import USER, PASSWORD, DB, HOST


async def create_post(post_name: str, post_description: str, post_image: str,
                      post_tag: str, user_name: str, create_date: str, create_time: str):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)
    try:
        await conn.execute(
            "INSERT INTO posts (post_name, post_description, post_image, post_tag, user_name, create_date, create_time) "
            "VALUES ($1, $2, $3, $4, $5, $6, $7)",
            post_name, post_description, post_image, post_tag, user_name, create_date, create_time
        )
    finally:
        await conn.close()
