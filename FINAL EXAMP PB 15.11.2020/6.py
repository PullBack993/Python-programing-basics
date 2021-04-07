location = int(input())

for i in range(location):
    counter = 0
    middle = int(input())
    day_location = int(input())
    for a in range (day_location):
        day_gold = float(input())
        counter += day_gold
    if middle <= (counter / day_location):
        print(f'Good job! Average gold per day: {counter / day_location:.2f}.')
    else:
        print(f'You need {middle - (counter / day_location):.2f} gold.')