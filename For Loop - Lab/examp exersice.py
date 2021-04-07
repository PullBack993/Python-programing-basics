import math
day = int(input())
food = float(input())
cat_food = 0
dog_food = 0
biscuits = 0
total_food = 0
total_day = 0
for i in range(1, day + 1):
    dog = int(input())

    cat = int(input())
    total_day += 1
    cat_food += cat
    dog_food += dog
    total_food += cat + dog
    if total_day == 3:
        biscuits += (cat + dog) * 0.1
        total_day = 0
print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{abs(total_food / food) * 100:.2f}% of the food has been eaten.')
print(f'{(dog_food / total_food ) * 100:.2f}% eaten from the dog.')
print(f'{(cat_food / total_food) * 100:.2f}% eaten from the cat.')