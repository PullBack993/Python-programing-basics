price_film = float(input())
num_stat = int(input())
price_clothing = float(input())

deko = price_film * 0.10
price = num_stat * price_clothing
total = deko + price

if num_stat > 150:
    action = price * 0.10
    total = total - action
if total > price_film:
    print(f"Not enough money!")
    print(f"Wingard needs {total - price_film:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {price_film - total:.2f} leva left.")
