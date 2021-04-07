record_sek = float(input())
distance_m = float(input())
time_sek_for_1m = float(input())

climp = distance_m * time_sek_for_1m
delap = (distance_m // 50) * 30
total = climp + delap

if total < record_sek:
    print(f'Yes! The new record is {total:.2} seconds')
else:
    print (f'No! He was {total - record_sek} seconds slower.')