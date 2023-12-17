from lexicon.ru_lexicon_funcs import reply_other_answers
from aiogram import Router
from aiogram.types import Message


router: Router = Router(name='Router2')


@router.message()
async def process_other_answers(message: Message) -> None:
    await message.answer(
        text=reply_other_answers()
    )