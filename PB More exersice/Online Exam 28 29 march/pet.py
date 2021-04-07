food = int(input())
kg_food = food * 1000
counter = 0
gr_food = input()
while gr_food != 'Adopted':
    a = int(gr_food)
    counter += a
    gr_food = input()

if kg_food >= counter:
    print(f'Food is enough! Leftovers: {abs(counter - kg_food)} grams.')
else:
    print(f'Food is not enough. You need {abs(kg_food - counter)} grams more.')