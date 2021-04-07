budget = float(input())
season = input()

if season == 'summer':
    if budget <= 100:
        budget = budget * 0.30
        print (f'Somewhere in Bulgaria')
        print (f'Camp - {budget:.2f}')
    elif budget <= 1000:
        budget = budget * 0.40
        print(f'Somewhere in Balkans')
        print(f'Camp - {budget:.2f}')
    elif budget > 1000:
        budget = budget * 0.90
        print(f'Somewhere in Europe')
        print(f'Hotel - {budget:.2f}')
if season == 'winter':
    if budget <= 100:
        budget = budget * 0.70
        print(f'Somewhere in Bulgaria')
        print(f'Hotel - {budget:.2f}')
    elif budget <= 1000:
        budget = budget * 0.80
        print(f'Somewhere in Balkans')
        print(f'Hotel - {budget:.2f}')
    elif budget > 1000:
        budget = budget * 0.90
        print(f'Somewhere in Europe')
        print(f'Hotel - {budget:.2f}')
