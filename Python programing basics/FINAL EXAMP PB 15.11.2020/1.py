one_print = float(input()) * 899
cover = float(input()) * 2
discount = int(input())
designer = float(input())
total_discount = int(input())
total_sum = (one_print + cover)
total_sum -= (total_sum * discount) / 100
coast_disayner = total_sum + designer
coast_disayner -= (coast_disayner * total_discount) / 100

print(f'Avtonom should pay {coast_disayner:.2f} BGN.')
