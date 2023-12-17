from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU


start_game_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['start game']
)
rock_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['rock']
)
paper_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['paper']
)
scissors_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['scissors']
)


subjects_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [rock_btn, paper_btn, scissors_btn]
    ],
    resize_keyboard=True
)


start_game_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[start_game_btn]],
    resize_keyboard=True
)