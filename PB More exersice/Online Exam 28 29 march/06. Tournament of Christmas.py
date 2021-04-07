day_tournament = int(input())
game_name = input()

count_win = 0
game_los = 0
game_win = 0
day_win = 0
day_los = 0
day = 0
while day_tournament > day:
    if game_name == 'Finish':
        day += 1
        if game_win > game_los:
            count_win += (game_win * 0.10) + game_win
            game_win = 0
            game_los = 0
            if day_tournament == day:
                break
            else:
                game_name = input()
        else:
            count_win += game_win
            game_win = 0
            game_los = 0
            if day_tournament == day:
                break
            else:
                game_name = input()

    result_game = input()

    if result_game == 'win':
        day_win += 1
        game_win += 20
    else:
        day_los += 1
        game_los += 20
    game_name = input()

if day_win > day_los:
    count_win += (0.20 * count_win)
    print(f'You won the tournament! Total raised money: {count_win:.2f}')

else:
    print(f'You lost the tournament! Total raised money: {count_win:.2f}')