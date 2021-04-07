hour = int(input())
minutes = int(input())

final_minutes = 0

if minutes < 45:
    final_minutes = minutes + 15
elif minutes >= 45:
    final_minutes = minutes + 15 - 60
    hour = hour + 1
if hour == 24:
    hour = 0

if final_minutes < 10:
    print(f'{hour}:0{final_minutes}')
else:
    print(f'{hour}:{final_minutes}')