from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    bot_token: str


@dataclass
class DatabaseConfig:
    host: str
    port: int
    name: str
    user: str
    password: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config() -> Config:
    
    env: Env = Env()
    env.read_env()

    return Config(
        tg_bot=TgBot(
            bot_token=env('BOT_TOKEN')
        ),
        db=DatabaseConfig(
            host=env('DB_HOST'),
            port=env.int('DB_PORT'),
            name=env('DATABASE'),
            user=env('DB_USER'),
            password=env('DB_PASSWORD')
        )
    )