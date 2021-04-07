num = int(input())
counter = 0

for x in range(num + 1):
    for x1 in range(num + 1):
        for x2 in range(num + 1):
            if x + x1 + x2 == num:
                counter += 1


print(counter)