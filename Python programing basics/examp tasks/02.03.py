import math

year = input()
holidays = int(input())
weekends = int(input())

saturday_games = (48 - weekends) * 3 / 4
holiday_games = holidays * 2 / 3
total_games = saturday_games + holiday_games + weekends

if year == 'leap':
    total_games += total_games * 0.15

print(math.floor(total_games))