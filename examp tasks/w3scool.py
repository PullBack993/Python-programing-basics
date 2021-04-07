piece = int(input())
total_people = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
for i in range(piece):
    people = int(input())
    if people <= 5:
        g1 += people

    elif people <= 12:
        g2 += people

    elif people <= 25:
        g3 += people

    elif people <= 40:
        g4 += people

    elif people >= 41:
        g5 += people

    total_people += people

print(f'{(g1/total_people)* 100:.2f}%')
print(f'{(g2/total_people)* 100:.2f}%')
print(f'{(g3/total_people)* 100:.2f}%')
print(f'{(g4/total_people)* 100:.2f}%')
print(f'{(g5/total_people)* 100:.2f}%')
