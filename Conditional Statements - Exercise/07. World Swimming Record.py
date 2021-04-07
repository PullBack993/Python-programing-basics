record_sec = float(input())
record_m = float(input())
time_sek_1m = float(input())

result = record_m * time_sek_1m
slower = (record_m // 15) * 12.5
result += slower

if result < record_sec:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {result - record_sec:.2f} seconds slower.')
