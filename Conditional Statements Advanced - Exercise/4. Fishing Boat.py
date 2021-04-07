budget = float(input())
season = input()
fisherman = int(input())

rent = 0
if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fisherman <= 6:
    rent -= rent * 0.1
elif fisherman <= 11:
    rent -= rent * 0.15
else:
    rent -= rent * 0.25

if fisherman % 2 == 0 and not season == 'Autumn':
    rent -= rent * 0.05

diff = abs(budget - rent)
if budget >= rent:
    print (f'Yes! You have {diff:.2f} leva left.')
else:
    print (f'Not enough money! You need {diff:.2f} leva.')