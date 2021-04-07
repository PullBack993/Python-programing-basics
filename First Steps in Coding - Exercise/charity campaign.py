day = float(input())
cook = float(input())
cake = float(input())
waffles = float(input())
pancakes = float(input())

cake = cake * 45
waffles = waffles * 5.80
pancakes = pancakes * 3.20

total_for_day = (cake+waffles+pancakes) * cook
campaign = total_for_day * day
all_days = campaign - (campaign/8)

print(all_days)
