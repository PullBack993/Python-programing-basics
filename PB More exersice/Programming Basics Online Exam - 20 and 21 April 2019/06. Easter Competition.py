import sys
bread = int(input())
max_point = -sys.maxsize
point = 0
counter = ""
for i in range(bread):
    point = 0
    name = input()
    rating = input()

    while rating != "Stop":
        rating = int(rating)
        point += rating
        rating = input()
    print(f"{name} has {point} points.")

    if max_point < point:
        max_point = point
        counter = name
        print(f'{name} is the new number 1!')

print(f'{counter} won competition with {max_point} points!')
