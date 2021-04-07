length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
liters = volume / 1000
liters -= liters * percent / 100
print(liters)