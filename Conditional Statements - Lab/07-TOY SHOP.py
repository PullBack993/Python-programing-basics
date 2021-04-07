price_trip = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_teddybear = int(input())
num_minion = int(input())
num_truck = int(input())


pr_puzz = num_puzzles * 2.60
pr_doll = num_dolls * 3
pr_ted = num_teddybear * 4.10
pr_min = num_minion * 8.20
pr_tru = num_truck * 2

total_toys = num_puzzles + num_dolls + num_teddybear + num_minion + num_truck
profit = pr_puzz + pr_doll + pr_ted + pr_min + pr_tru

if total_toys >= 50:
    discount = 0.75 * profit
    rent = discount * 0.1
    money_left = discount - rent
    money_left_final = abs(money_left)
    if money_left_final >= price_trip:
        print(f'Yes! {money_left_final - price_trip:.2f} lv left.')
    else:
        print(f'Not enough money! {price_trip - money_left_final:.2f} lv needed.')
else:
    rent_new = profit * 0.10
    money_lef_new = profit - rent_new
    money_new_final = abs(money_lef_new)
    if money_new_final >= price_trip:
        print(f'Yes! {money_new_final - price_trip:.2f} lv left.')
    else:
        print(f'Not enough money! {price_trip - money_new_final:.2f} lv needed.')