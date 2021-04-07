total = float(input())
gender = input()
age = int(input())
sport = input()
sum = 0
if gender == 'm':
    if sport == 'Gym':
       sum = 42
    elif sport == 'Boxing':
        sum = 41
    elif sport == 'Yoga':
        sum = 45
    elif sport == 'Zumba':
        sum = 34
    elif sport == 'Dances':
        sum = 51
    elif sport == 'Pilates':
        sum = 39
elif gender == 'f':
    if sport == 'Gym':
       sum = 35
    elif sport == 'Boxing':
        sum = 37
    elif sport == 'Yoga':
        sum = 42
    elif sport == 'Zumba':
        sum = 31
    elif sport == 'Dances':
        sum = 53
    elif sport == 'Pilates':
        sum = 37
if age <= 19:
    sum *= 0.80
if total > sum:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f"You don't have enough money! You need ${abs(total - sum):.2f} more.")