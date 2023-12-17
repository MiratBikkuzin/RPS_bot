from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from models.methods import db_connection
from keyboards.set_menu import set_main_menu

from aiogram import Bot, Dispatcher
import asyncio


async def main() -> None:

    config: Config = load_config()
    bot: Bot = Bot(config.tg_bot.bot_token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    pool, connection = await db_connection(
        running_loop=asyncio.get_running_loop(),
        config=config
    )

    async with connection:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())