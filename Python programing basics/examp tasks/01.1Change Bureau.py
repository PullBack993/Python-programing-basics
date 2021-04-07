num_bitcoin = float(input())
china_yuan = float(input())
comision = float(input())

bit = num_bitcoin * 1168
china = china_yuan * 0.15 * 1.76
total = bit + china
change = total / 1.95
taksa = change * comision / 100
end_sum = change - taksa

print(f'{end_sum:.2f}')