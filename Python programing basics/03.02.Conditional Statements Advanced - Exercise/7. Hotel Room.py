month = input()
overnight = int(input())

apartment = None
studio = None

if month == 'May' or month == 'October':
    apartment = 65
    studio = 50
    studio_rent = studio * overnight
    apartment_rent = apartment * overnight
    if overnight > 14:
        apartment_rent *= 0.90
        studio_rent *= 0.70
    elif overnight > 7:
        studio_rent *= 0.95

elif month == 'June' or month == 'September':
    apartment = 68.70
    studio = 75.20
    studio_rent = studio * overnight
    apartment_rent = apartment * overnight
    if overnight > 14:
        apartment_rent *= 0.90
        studio_rent *= 0.80

elif month == 'July' or month == 'August':
    apartment = 77
    studio = 76
    studio= studio * overnight
    apartment= apartment * overnight
    if overnight > 14:
        apartment *= 0.90

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')

