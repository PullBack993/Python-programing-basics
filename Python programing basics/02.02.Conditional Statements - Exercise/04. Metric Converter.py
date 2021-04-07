number = float(input())
first = str(input())
second = str(input())

if first == "mm":
    number_mm = number
elif first == "cm":
    number_mm = number * 10
else:
    number_mm = number * 1000

if second == "mm":
    output_number = number_mm
elif second == "cm":
    output_number = number_mm / 10
else:
    output_number = number_mm / 1000

print(f"{output_number: .3f}")