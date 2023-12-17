def reply_start_command(first_name: str, old_user: bool) -> str:

    if old_user:
        return f"Я тебя помню {first_name}! Сыграем снова в рак пэйпер сизорс как в былые 90-е?"
    
    return f"Привет {first_name}! Я бот, который сыграет с тобой в камень, ножницы, бумага!" \
            " Чтобы сыграть со мной жми на кнопку ⬇️"


def reply_play_command() -> str:
    return f"Игра началась! Твой ход первый! Выбирай камень, ножницы или бумагу ⬇️"


def reply_statistic_command(full_name: str, total_games: int, wins: int,
                            game_score: int, win_rate: str, emoticons: tuple[str]) -> str:
    
    game_emo, winner_cup_emo, score_emo, win_rate_emo = emoticons

    return f"Статистика игрока {full_name}\n\n" \
           f"{game_emo} Всего сыграно игр: {total_games} {game_emo}\n\n" \
           f"{winner_cup_emo} Всего выиграно игр: {wins} {winner_cup_emo}\n\n" \
           f"{score_emo} Всего заработано очков: {game_score} {score_emo}\n\n" \
           f"{win_rate_emo} Процент побед: {win_rate} {win_rate_emo}"


def reply_myplace_command(user_place: int, user_places_emo: str) -> str:
    return f'{user_places_emo} Ваша позиция среди других пользователей: {user_place} {user_places_emo}'


def reply_unblocked_bot() -> str:
    return 'Я рад видеть тебя снова!'


def reply_other_answers() -> str:
    return 'Моя твоя не понимать! Давай просто сыграем в игру!!!'