LEXICON_RU: dict[str: str, str: str] = {
    'start game': '🎮Сыграем!🎮',
    'not_start': 'Не хочу!',
    'rock': '🪨Камень🪨',
    'paper': '📄Бумага📄',
    'scissors': '✂️Ножницы✂️'
}


OPPOSITE_SUBJECTS_RU: dict[str: str, str: str] = {
    LEXICON_RU['rock']: LEXICON_RU['paper'],
    LEXICON_RU['paper']: LEXICON_RU['scissors'],
    LEXICON_RU['scissors']: LEXICON_RU['rock']
}