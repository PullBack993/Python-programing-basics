width = int(input())
length = int(input())

total = width * length
line = input()
while line != 'STOP':
    line = int(line)
    total -= line
    if total < 1:
        break
    line = input()

if total >= 1:
    print(f'{total} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total)} pieces more.')
