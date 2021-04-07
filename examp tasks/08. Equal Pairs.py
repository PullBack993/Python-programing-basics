n = int(input())
number = 0
prev_sum = 0
diff = 0
max_diff = 0

for i in range(1, n + 1):
    number += int(input())
    number += int(input())

    if i > 1:
        diff = abs(number - prev_sum)

    if diff > max_diff:
        max_diff = diff
    prev_sum = number
    number = 0

if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")