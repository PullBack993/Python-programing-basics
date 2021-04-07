lili = int(input())
#ne ceten igracka
#ceten pari vseki vtori x 10
#za prodadena igracka P za X pari
#kolko pari e sibrala i dali moje da si kupi peralnq

price_machine = float(input())
toy_price = int(input())

num_of_toy = 0
saved_money = 0              #pri progresivno narastvane pri for cikil trqbva da slojim 2 promenlivi !!!
money_for_birthday = 10

for i in range(1, lili + 1):
    if i % 2 == 0:      #0  9+19+29+39+49
    #ili #saved_money += (i * 10 /2) - 1
        saved_money += (money_for_birthday - 1)
        money_for_birthday += 10
    else:
        #save_money += toy_price
        num_of_toy += 1
saved_money += num_of_toy * toy_price
if saved_money >= price_machine:
    print(f'Yes! {saved_money - price_machine:.2f}')
else:
    print(f'No! {abs(saved_money - price_machine):.2f}')

