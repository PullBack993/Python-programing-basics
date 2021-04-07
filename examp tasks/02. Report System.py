sum_for_charity = int(input())
average_cs = 0
average_cc = 0
total_money = 0
counter = 0
while sum_for_charity > total_money:
    pay = input()
    if pay == 'End':
        break
    pay = int(pay)
    counter += 1
    if counter == 2:
        counter = 0
        if pay < 10:
            print(f'Error in transaction!')
        else:
            average_cc += pay
            total_money += pay
            print(f'Product sold!')

    else:
        if pay > 100:
            print(f'Error in transaction!')
        else:
            average_cs += pay
            total_money += pay
            print(f'Product sold!')

if total_money >= sum_for_charity:
    print(f'Average CS: {average_cs / 2:.2f}')
    print(f'Average CC: {average_cc / 2:.2f}')
else:
    print(f'Failed to collect required money for charity.')
