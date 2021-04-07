all_food = int(input()) * 1000
counter = 0
day_food = input()
while day_food != 'Adopted':
    food = int(day_food)
    counter += food
    day_food = input()
if all_food >= counter:
    print(f'Food is enough! Leftovers: {all_food - counter} grams.')
else:
    print(f'Food is not enough. You need {counter - all_food} grams more.')