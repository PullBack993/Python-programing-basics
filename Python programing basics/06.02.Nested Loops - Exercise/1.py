n = int(input())
num = 1
is_bigger = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if num > n:
            is_bigger = True
            break
        print(num, end=' ')
        num += 1
    if is_bigger:
        break
    print()