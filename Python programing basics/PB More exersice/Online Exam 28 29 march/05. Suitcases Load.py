kit = float(input())
place = input()
counter = 0
count = 0 - kit
b = 0
pack = 0
while place != "End":
    place = float(place)
    b += place
    if kit <= b:
        break

    pack += 1
    counter += 1

    if counter == 3:
        count += place
        a = place * 0.10
        count += a
        counter = 0
    else:
        count += place
    place = input()
if place == "End":
    print("Congratulations! All suitcases are loaded!")
elif kit <= b:
    print('No more space!')

print(f'Statistic: {pack} suitcases loaded.')