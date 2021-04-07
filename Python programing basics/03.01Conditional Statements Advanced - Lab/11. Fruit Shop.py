# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	2.70	5.50	3.85

fruit = input()
day = input()
volume = float(input())
price = 0
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day =='Friday':
    if fruit == 'banana':
        price = 2.50
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'apple':
        price = 1.20
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'orange':
        price = 0.85
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'kiwi':
        price = 2.70
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'pineapple':
        price = 5.50
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'grapes':
        price = 3.85
        fruit = price * volume
        print(f'{fruit:.2f}')
    else:
        print('error')
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'apple':
        price = 1.25
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'orange':
        price = 0.90
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'grapefruit':
        price = 1.60
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'kiwi':
        price = 3.00
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'pineapple':
        price = 5.60
        fruit = price * volume
        print(f'{fruit:.2f}')
    elif fruit == 'grapes':
        price = 4.20
        fruit = price * volume
        print(f'{fruit:.2f}')
    else:
        print('error')
else:
    print('error')
