square_meters = float(input())

need_money = square_meters * 7.61
the_discount = need_money * 0.18
end_sum = need_money - the_discount

print(f'The final price is: {end_sum} lv. \n The discount is: {the_discount} lv.')