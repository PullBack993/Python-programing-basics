num_of_bottles = int(input())
total_bottles = num_of_bottles * 750
total_dishes = 0
total_dishes2 = 0
counter_dishes = 0
counter = 0
while total_bottles >= 0:
    dishes = input()
    if dishes == 'End':
        break
    dishes = int(dishes)
    counter_dishes += dishes
    counter += 1
    if counter == 3:
        b = dishes * 15
        total_dishes2 += dishes
        total_dishes += b
        counter = 0
        total_bottles -= b
    else:
        a = dishes * 5
        total_dishes += a
        total_bottles -= a
if total_bottles >= 0:
    print(f"Detergent was enough!")
    print(f"{counter_dishes - total_dishes2} dishes and {total_dishes2} pots were washed.")
    print(f"Leftover detergent {total_bottles} ml.")
else:
    print(f'Not enough detergent, {abs(total_bottles)} ml. more necessary!')