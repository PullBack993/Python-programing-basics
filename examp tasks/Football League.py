stadium = int(input())
fans = int(input())
f_a = 0
f_b = 0
f_v = 0
f_g = 0

for i in range(fans):
    sector = input()
    if sector == 'A':
        f_a += 1
    elif sector == 'B':
        f_b += 1
    elif sector == 'V':
        f_v += 1
    elif sector == 'G':
        f_g += 1

print(f'{f_a / fans * 100:.2f}%')
print(f'{f_b / fans * 100:.2f}%')
print(f'{f_v / fans * 100:.2f}%')
print(f'{f_g / fans * 100:.2f}%')
print(f'{fans / stadium * 100:.2f}%')