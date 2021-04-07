import sys
n = int(input())

#tuka ne cetem dali cisloto e cetno ili ne cetno
#sonder cetem dali poziciqta "i" e na cetno ili ne cetna poziciq

odd_sum = 0
even_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    else:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

print(f'OddSum={odd_sum:.2f},')

if odd_min != sys.maxsize:
    print(f'OddMin={odd_min:.2f},')
else:
    print('OddMin=No,')

if odd_max != -sys.maxsize:
    print(f'OddMax={odd_max:.2f},')
else:
    print('OddMax=No,')

print(f'EvenSum={even_sum:.2f},')

if even_min != sys.maxsize:
    print(f'EvenMin={even_min:.2f},')
else:
    print(f'EvenMin=No,')

if even_max != -sys.maxsize:
    print(f'EvenMax={even_max:.2f}')
else:
    print(f'EvenMax=No')
