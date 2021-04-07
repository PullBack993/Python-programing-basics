import math
n = int(input())
for a in range(n // 2):
    starts = 1
    if n % 2 == 0:
        starts += 1
    roof_length = math.ceil(n / 2)
    padding = (n - starts) // 2
    line = '-' * padding \
        + '*' * starts \
        + '-' * padding
    print(line)
for i in range(n // 2):
    line = '|' + '*' * (n - 2) + '|'
    print(line)
