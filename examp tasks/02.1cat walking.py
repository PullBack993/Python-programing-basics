walking_time = int(input())
num_walks = int(input())
calories = int(input())

burn_calories = (num_walks * walking_time) * 5
calories = calories * 50/100

if burn_calories >= calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burn_calories}."')