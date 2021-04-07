import math
year = input()
holiday = int(input())
hometown = int(input())

weekend = 48 - hometown
sofia = weekend - hometown

weekend = weekend * 0.75 + hometown
holiday_play = holiday * 0.66667
total = weekend + holiday_play

if year == 'leap':
    end = total * 0.15
    end_total = end + total
    print(f'{math.floor(end_total)}')
else:
    print(f'{math.floor(total)}')