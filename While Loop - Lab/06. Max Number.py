import sys
n = input()
num = -sys.maxsize
while n != 'Stop':
    nom = int(n)

    if nom > num:
        num = nom
    n = input()

print (num)