month = input()
time = int(input())
people = int(input())
day = input()
price = 0
if month == 'march' or month == 'april' or month == 'may':
    if day == 'day':
        price = 10.50
    else:
        price = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if day == 'day':
        price = 12.60
    else:
        price = 10.20

if people > 4:
    price = price * 0.90
    if time >= 5:
        discount_price = price * 0.50
        print(f'Price per person for one hour: {discount_price:.2f}')
    else:
        print(f'Price per person for one hour: {price:.2f}')
else:
    print(f'Price per person for one hour: {price:.2f}')
if time >= 5:
    final_price = price * 0.50
    print(f'Total cost of the visit: {(final_price * people) * time:.2f}')
else:
    print(f'Total cost of the visit: {(price * people)* time:.2f}')
