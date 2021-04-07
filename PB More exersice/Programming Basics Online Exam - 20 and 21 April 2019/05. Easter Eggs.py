import sys
egg = int(input())
red = 0
orange = 0
blue = 0
green = 0
total = 0
colors = ""
max_egg = -sys.maxsize
for i in range(egg):
    color = input()
    total += 1
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1

if max_egg < red:
    max_egg = red
    colors = 'red'
if max_egg < orange:
    max_egg = orange
    colors = 'orange'
if max_egg < blue:
    max_egg = blue
    colors = 'blue'
if max_egg < green:
    max_egg = green
    colors = 'green'

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max_egg} -> {colors}')