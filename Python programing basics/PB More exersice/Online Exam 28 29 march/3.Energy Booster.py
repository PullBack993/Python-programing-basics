fruit = input()
size = input()
num = int(input())
price = 0
if size == 'small':
    num *= 2
    if fruit == 'Watermelon':
        price = 56
    elif fruit == 'Mango':
        price = 36.66
    elif fruit == 'Pineapple':
        price = 42.10
    elif fruit == 'Raspberry':
        price = 20
elif size == 'big':
    num *= 5
    if fruit == 'Watermelon':
        price = 28.70
    elif fruit == 'Mango':
        price = 19.60
    elif fruit == 'Pineapple':
        price = 24.80
    elif fruit == 'Raspberry':
        price = 15.20

total = price * num

if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5
print(f'{total:.2f} lv.')
