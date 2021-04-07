the_deposit_amount = float(input())
time_deposit = int(input())
year_rate = float(input())

amount = the_deposit_amount+time_deposit * ((the_deposit_amount * year_rate / 100) / 12)

print(amount)