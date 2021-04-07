destination = input()

#ako slojim tuka spend_money togava nqma da se zanuli kogato izl izvin cikala
while destination != 'End':
    need_money = float(input()) #i dvete trqbva da sa v cikila
    #tiy kato e dadeno v uslovieto !!!
    spend_money = 0
    while spend_money < need_money:
        money = float(input())
        spend_money += money
    else:
        print(f'Going to {destination}!')

    destination = input()