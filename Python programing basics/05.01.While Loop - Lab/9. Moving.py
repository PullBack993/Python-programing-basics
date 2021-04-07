width = int(input())
langth = int(input())
height = int(input())

volume = width * langth * height
command = input()

while command != "Done":

    boxes = int(command)
    volume -= boxes

    if volume <= 0:
        print(f'No more space! You need {abs(volume)} Cubic meters more.')

    command = input()

if volume >= 0:
    print(f'{volume} Cubic meters left.')