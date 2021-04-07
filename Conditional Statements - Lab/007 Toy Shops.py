trip_price = float(input())

num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

pr_puzzles = num_puzzles * 2.6
pr_dolls = num_dolls * 3
pr_bears = num_bears * 4.10
pr_minions = num_minions * 8.20
pr_trucks = num_trucks * 2

order_items = num_puzzles + num_dolls + num_bears + num_minions + num_trucks

if order_items >= 50:
    discount = 0.75
else:
    discount = 1

subtotal = pr_puzzles + pr_dolls + pr_bears + pr_minions + pr_trucks

total = subtotal * discount
total *= 0.9

income = total - trip_price

if income >= 0:
    print(f"Yes! {income:.2f} lv left.")
else:
    income *= -1
    print(f"Not enough money! {income:.2f} lv needed.")

