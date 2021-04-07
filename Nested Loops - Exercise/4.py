people = int(input())
total_presentation = 0
name = input()
total_grades = 0
while name != 'Finish':
    total_sum = 0

    for i in range(1, people + 1):
        grade = float(input())
        total_sum += grade
    print(f"{name} - {total_sum / people:.2f}.")
    total_presentation += 1
    total_grades += total_sum
    name = input()

print(f"Student's final assessment is {total_grades / (total_presentation * people):.2f}.")