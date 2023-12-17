from models.methods import execute_query
from models.db_queries import *
from keyboards import start_game_keyboard, subjects_keyboard
from lexicon.ru_lexicon_funcs import *
from lexicon.lexicon_ru import LEXICON_RU, OPPOSITE_SUBJECTS_RU
from emojize import game_emo, user_places_emo, score_emo, win_rate_emo, winner_cup_emo

from aiogram.filters import Command, CommandStart, MEMBER, KICKED, ChatMemberUpdatedFilter
from aiogram.types import Message, ChatMemberUpdated
from aiogram import Router
from random import choice


router: Router = Router(name='Router1')


@router.message(CommandStart())
async def proccess_start_command(message: Message) -> None:
    
    user_id: int = message.from_user.id
    firstname: str = message.from_user.first_name
    old_user: bool = True

    if not await execute_query(select_game_info_query, 'SELECT', user_id):
        old_user: bool = False
        await execute_query(add_user_query, 'INSERT',
                            user_id, message.from_user.username, firstname, 0, 0, 0, '100%', 'Active')
        
    await message.answer(
        text=reply_start_command(firstname, old_user),
        reply_markup=start_game_keyboard
    )
        
        


@router.message(Command(commands=['play']))
@router.message(lambda x: 'сыграем' in x.text.lower())
async def proccess_play_command(message: Message) -> None:
    await message.answer(
        text=reply_play_command(),
        reply_markup=subjects_keyboard
    )


@router.message(lambda x: x.text in (LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']))
async def process_subject_message(message: Message) -> None:

    rock, paper, scissors = LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']
    random_subject: str = choice((rock, paper, scissors))
    user_subject: str = message.text
    user_id: int = message.from_user.id

    if random_subject == user_subject:
        await message.answer(
            text='Ничья! Продолжаем дальше!'
        )
        return
    
    total_games, wins, _, _ = await execute_query(select_game_info_query, 'SELECT', user_id)
    
    if OPPOSITE_SUBJECTS_RU[user_subject] == random_subject:
        increase_wins: int = 0
        increase_game_score: int = -500
        win_rate: str = str(round((wins / (total_games + 1)) * 100)) + '%'
        answer_text: str = f'{random_subject}' \
                            'Я выйграл!'        

    else:
        increase_wins: int = 1
        increase_game_score: int = 1000
        win_rate: str = str(round(((wins + 1) / (total_games + 1)) * 100)) + '%'
        answer_text: str = f'{random_subject}' \
                            'Я проиграл😢'
        
    await execute_query(update_user_info_query, 'UPDATE',
                        increase_wins, increase_game_score, win_rate, user_id)
    await message.answer(answer_text)


@router.message(Command(commands=['statistic']))
async def proccess_statistic_command(message: Message) -> None:
    
    emoticons: tuple[str, str] = (game_emo, winner_cup_emo, score_emo, win_rate_emo)
    fullname: str = message.from_user.full_name
    total_games, wins, game_score, win_rate = await execute_query(select_game_info_query, 'SELECT',
                                                                  message.from_user.id)
    
    await message.answer(
        text=reply_statistic_command(fullname, total_games, wins, game_score, win_rate, emoticons)
    )


@router.message(Command(commands=['myplace']))
async def proccess_place_command(message: Message) -> None:
    
    user_place: int = int((await execute_query(select_user_place_query, 'SELECT', message.from_user.id))[0])

    await message.answer(
        text=reply_myplace_command(user_place, user_places_emo)
    )


@router.my_chat_member(ChatMemberUpdatedFilter(KICKED))
async def proccess_kicked_user(event: ChatMemberUpdated) -> None:
    await execute_query(rename_status_user_query, 'UPDATE',
                        'Inactive', event.from_user.id)
    

@router.my_chat_member(ChatMemberUpdatedFilter(MEMBER))
async def proccess_member_user(event: ChatMemberUpdated) -> None:
    await execute_query(rename_status_user_query, 'UPDATE',
                        'Active', event.from_user.id)
    await event.answer(reply_unblocked_bot())