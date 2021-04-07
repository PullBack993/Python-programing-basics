count_cat = int(input())
group1 = 0
group2 = 0
group3 = 0
total_food = 0
import math
for i in range(count_cat):
    gram_food = float(input())
    total_food += gram_food
    if 100 <= gram_food < 200:
        group1 += 1
    elif 200 <= gram_food < 300:
        group2 += 1
    elif 300 <= gram_food < 400:
        group3 += 1
print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f'Price for food per day: {(total_food / 1000) * 12.45:.2f} lv.')