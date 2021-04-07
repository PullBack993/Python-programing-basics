failed = int(input())
number_of_problems = 0
Last_problem = ''
failed_times = 0
average_score = 0
name_problem = input()

while name_problem != 'Enough':
    grade = int(input())
    if grade <= 4:
        failed_times += 1
        if failed == failed_times:
            print(f"You need a break, {failed_times} poor grades.")
            break

    average_score += grade
    number_of_problems += 1
    Last_problem = name_problem

    name_problem = input()

if failed != failed_times:
    print(f'Average score: {(average_score / number_of_problems):.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {Last_problem}')

