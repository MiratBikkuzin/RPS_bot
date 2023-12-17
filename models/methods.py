from config_data.config import Config
from aiomysql.utils import _PoolAcquireContextManager
from asyncio import ProactorEventLoop
import aiomysql


async def db_connection(running_loop: ProactorEventLoop, config: Config) -> tuple[aiomysql.Pool, _PoolAcquireContextManager]:
    global connection

    pool: aiomysql.Pool = await aiomysql.create_pool(
        loop=running_loop,
        host=config.db.host,
        port=config.db.port,
        db=config.db.name,
        user=config.db.user,
        password=config.db.password,
        autocommit=True
    )

    async with pool.acquire() as connection:
        pass

    return pool, connection


async def execute_query(query: str, main_command: str, *args) -> tuple | None:
    async with connection.cursor() as cursor:
        await cursor.execute(query, args)
        if main_command.lower() == 'select':
            return await cursor.fetchone()