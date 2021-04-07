counter_client = int(input())

total = 0
total_price = 0
counter = 0
for i in range (1, counter_client+1):
    buy_client = input()

    while buy_client != 'Finish':
        counter += 1
        if buy_client == 'basket':
            total_price += 1.50
        elif buy_client == 'wreath':
            total_price += 3.80
        elif buy_client == 'chocolate bunny':
            total_price += 7
        buy_client = input()
    if counter % 2 == 0:
        total_price *= 0.80
    total += total_price
    print(f'You purchased {counter} items for {total_price:.2f} leva.')
    counter = 0
    total_price = 0

print(f'Average bill per client is: {total / counter_client:.2f} leva.')