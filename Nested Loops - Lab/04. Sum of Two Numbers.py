start_num = int(input())
end_number = int(input())
magic_num = int(input())
counter = 0
is_found = False

for first in range(start_num, end_number + 1):
    for second in range(start_num, end_number + 1):
        counter += 1
        if first + second == magic_num:
            is_found = True
            print(f'Combination N:{counter} ({first} + {second} = {magic_num})')
            break
    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_num}")