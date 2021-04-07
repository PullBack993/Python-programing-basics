money_needed = float(input())
available_money = float(input())

counter = 0
total_day = 0
while available_money < money_needed:
    action = input()
    amount = float(input())
    total_day += 1

    if action == 'save':
        available_money += amount
        counter = 0
    else:
        counter += 1

        if available_money - amount > 0:
            available_money -= amount
        else:
            available_money = 0
        if counter == 5:
            print(f'You can\'t save the money.')
            print(f'{total_day}')
            break

if money_needed <= available_money:
    print(f'You saved the money for {total_day} days.')