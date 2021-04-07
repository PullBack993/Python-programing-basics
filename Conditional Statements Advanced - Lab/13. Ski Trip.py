day_stay = float(input())
room = input()
rating = input()
discount = 0

if room == 'room for one person':
    cost = (day_stay-1) * 18
    if rating == 'positive':
        total = cost + (cost * 0.25)
        print(f'{total:.2f}')
    elif rating == 'negative':
        total = cost - (cost * 0.10)
        print(f'{total:.2f}')

if room == 'apartment':
    cost = (day_stay-1) * 25
    if 10 > day_stay:
        discount = cost - (cost * 0.30)
    elif 10 <= day_stay <= 15:
        discount = cost - (cost * 0.35)
    elif day_stay > 15:
        discount = cost - (cost * 0.50)
    if rating == 'positive':
        discount += discount * 0.25
        print(f'{discount:.2f}')
    elif rating == 'negative':
        discount -= discount * 0.10
        print(f'{discount:.2f}')
if room == 'president apartment':
    cost = (day_stay-1) * 35
    if 10 > day_stay:
        discount = cost - (cost * 0.10)
    elif 10 <= day_stay <= 15:
        discount = cost - (cost * 0.15)
    elif day_stay > 15:
        discount = cost - (cost * 0.20)
    if rating == 'positive':
        discount += discount * 0.25
        print(f'{discount:.2f}')
    elif rating == 'negative':
        discount -= discount * 0.10
        print(f'{discount:.2f}')
