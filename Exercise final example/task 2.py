import math
name = input()
log = int(input())
pause = int(input())
mid_pause = 1 / 8 * pause
rest = 1 / 4 * pause
total = mid_pause + rest + log

if total <= pause:
    print(f'You have enough time to watch {name} and left with {math.ceil(pause - total)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(total - pause)} more minutes.")