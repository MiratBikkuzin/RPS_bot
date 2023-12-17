select_game_info_query: str = """
SELECT `total_games`, `wins`, `game_score`, `win_rate`
FROM users_info
WHERE %s = user_id"""


add_user_query: str = """
INSERT INTO `users_info` (`user_id`, `username`, `firstname`, `total_games`, `wins`, `game_score`, `win_rate`, `user_status`)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""


update_user_info_query: str = """
UPDATE `users_info`
SET `total_games` = `total_games` + 1,
    `wins` = `wins` + %s,
    `game_score` = `game_score` + %s,
    `win_rate` = %s
WHERE `user_id` > 0 AND %s = `user_id`"""


rename_status_user_query: str = """
UPDATE `users_info`
SET `user_status` = %s
WHERE `user_id` > 0 AND %s = `user_id`"""


select_user_place_query: str = """
SELECT `num`
FROM (
    SELECT row_number() over(ORDER BY `game_score` DESC, `win_rate` DESC) AS `num`, `user_id`
    FROM `users_info`
    ORDER BY `game_score` DESC, `win_rate` DESC
    ) help_query
WHERE %s = `user_id`
"""