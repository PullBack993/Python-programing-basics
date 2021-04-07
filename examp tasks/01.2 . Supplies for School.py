pens = float(input())
marker = float(input())
wash = float(input())
discount = int(input())

pens = pens * 5.80
marker = marker * 7.20
wash = wash * 1.20
all_coast = pens + marker + wash
total = all_coast - ((all_coast * discount ) / 100 )
print(f'{total:.3f}')