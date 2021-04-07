income = float(input())
grades = float(input())
salary = float(input())
import math
exelent = 0
social = 0

if grades >= 5.50:
    exelent += grades * 25 # 5.50*25 = 137.5

if income < salary and grades > 4.50:
    social += salary * 0.35

if social > exelent:
    print(f'You get a Social scholarship {math.floor(social)} BGN')
elif exelent >= social:
    if exelent != 0:
        print(f'You get a scholarship for excellent results {math.floor(exelent)} BGN')
    else:
        print (f'You cannot get a scholarship!')