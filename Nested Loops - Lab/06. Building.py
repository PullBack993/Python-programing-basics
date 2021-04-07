floors = int(input())
rooms = int(input())

for a in range(floors, 0, -1):
    for i in range(rooms):
        if a == floors:
            print(f'L{a}{i}', end=' ')
        elif a % 2 == 0:
            print(f'O{a}{i}', end=" ")
        elif a % 2 == 1:
            print(f'A{a}{i}', end=" ")
    print()