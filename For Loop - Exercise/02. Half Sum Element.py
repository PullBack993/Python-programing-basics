import  sys

n = int(input())

max_num = -sys.maxsize
sum_num = 0

for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_num += num

total_sum = sum_num - max_num

if total_sum == max_num:
    print('Yes')
    print(f'Sum = {total_sum}')
else:
    print('No')
    print(f'Diff = {abs(max_num - total_sum)}')