target = 10000
total_steps = 0
while total_steps < target:
    step = input()
    if step == 'Going home':
        step = int(input())
        total_steps += step
        break
    total_steps += int(step)
diff = abs(total_steps - target)
if total_steps >= target:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')