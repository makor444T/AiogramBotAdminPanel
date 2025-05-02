import asyncpg

from config.bot_config import USER, PASSWORD, DB, HOST


async def create_admin(user_id: int, user_name: str):
    conn = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, database=DB)

    user_exists = await conn.fetchval(
        "SELECT EXISTS(SELECT 1 FROM users WHERE user_id = $1)", user_id
    )

    if user_exists:
        await conn.execute(
            "UPDATE users SET user_name = $1, user_role = 'admin' WHERE user_id = $2",
            user_name, user_id
        )
    else:
        await conn.execute(
            "INSERT INTO users (user_id, user_name, user_role) VALUES ($1, $2, $3)",
            user_id, user_name, 'admin'
        )

    await conn.close()
