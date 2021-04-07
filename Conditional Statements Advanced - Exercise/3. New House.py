flower_type = input()
count = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    price = 5
    if count > 80:
        price -= price * 0.1  # price = price - price * 0.1
elif flower_type == 'Dahlias':
    price = 3.80
    if count > 90:
        price -= price * 0.15
elif flower_type == 'Tulips':
    price = 2.80
    if count > 80:
        price -= price * 0.15
elif flower_type == 'Narcissus':
    price = 3
    if count < 120:
        price += price * 0.15
elif flower_type == 'Gladiolus':
    price = 2.50
    if count < 80:
        price += price * 0.20

money_need = count * price
(total) = abs(money_need - budget)

if budget >= money_need:
    print(f'Hey, you have a great garden with {count} {flower_type} and {total:.2f} leva left.')
else:
    print(f'Not enough money, you need {total:.2f} leva more.')