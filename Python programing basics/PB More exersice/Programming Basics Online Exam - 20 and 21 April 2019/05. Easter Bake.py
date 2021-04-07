import sys
import math
bread = int(input())
counter_sugar = 0
counter_flour = 0

max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for i in range(bread):
    sugar = int(input())
    flour = int(input())
    counter_sugar += sugar
    counter_flour += flour
    if max_sugar < sugar:
        max_sugar = sugar
    if max_flour < flour:
        max_flour = flour
print(f'Sugar: {math.ceil(counter_sugar / 950)}')
print(f'Flour: {math.ceil(counter_flour / 750)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')