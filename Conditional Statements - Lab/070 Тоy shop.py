puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
tir = 2

vacation_price = float(input())
amount_of_puzzles = int(input())
amount_of_talking_dolls = int(input())
amount_of_teddy_bears = int(input())
amount_of_minions = int(input())
amount_of_tirs = int(input())

income = (puzzle * amount_of_puzzles) + (talking_doll * amount_of_talking_dolls) + (
            teddy_bear * amount_of_teddy_bears) + (minion * amount_of_minions) + (tir * amount_of_tirs)

total_order = amount_of_tirs + amount_of_teddy_bears + amount_of_minions + amount_of_talking_dolls + amount_of_puzzles

if total_order >= 50:
    discount = income * 0.25
else:
    discount = 0

profit = income - discount
rent = profit * 0.10
profit -= rent

if profit > vacation_price:
    money_left = profit - vacation_price
    print(f'Yes! {money_left:.2f}  lv left.')

elif profit <= vacation_price:
    money_in_need = vacation_price - profit
    print(f'Not enough money! {money_in_need:.2f} lv needed.')