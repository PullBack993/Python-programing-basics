count_day = int(input())
count_hour_day = int(input())
total = 0
for day in range(1, count_day + 1):
    sum_day = 0
    for hour in range(1, count_hour_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            sum_day += 2.50
        elif day % 2 == 1 and hour % 2 == 0:
            sum_day += 1.25
        else:
            sum_day += 1

    print(f'Day: {day} - {sum_day:.2f} leva')
    total += sum_day

print(f'Total: {total:.2f} leva')