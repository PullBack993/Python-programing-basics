move_name = input()
total = 0
student = 0
standard = 0
kid = 0

while move_name != 'Finish':
    free_place = int(input())
    tickets_sold = 0
    ticket = input()
    while ticket != 'End':
        tickets_sold += 1
        total += 1
        if ticket == 'student':
            student += 1
        elif ticket == 'standard':
            standard += 1
        elif ticket == 'kid':
            kid += 1
        if tickets_sold == free_place:
            break
        ticket = input()

    print(f'{move_name} - {tickets_sold / free_place * 100:.2f}% full.')
    move_name = input()

print(f'Total tickets: {total}')
print(f'{student/ total * 100:.2f}% student tickets.')
print(f'{standard/total * 100:.2f}% standard tickets.')
print(f'{kid / total * 100:.2f}% kids tickets.')