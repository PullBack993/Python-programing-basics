data = input()
balance = 0.0
while data != "NoMoreMoney":
    amount = float(data)
    if amount < 0:
        print('Invalid operation!')
        break
    balance += amount
    print(f"Increase: {amount:.2f}")
    data = input()

print(f"Total: {balance:.2f}")