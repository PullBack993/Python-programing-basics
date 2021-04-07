N1 = int(input())
N2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
    result = 0
    if operator == '+':
        result = N1 + N2
    elif operator == '-':
        result = N1 - N2
    else:
        result = N1 * N2
    if result % 2 == 0:
        print(f'{N1} {operator} {N2} = {result} - even')
    else:
        print(f'{N1} {operator} {N2} = {result} - odd')
elif operator == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        print(f'{N1} / {N2} = {N1/N2:.2f}')
elif operator == '%':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        print(f'{N1} % {N2} = {N1%N2}')



