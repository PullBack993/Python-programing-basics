name = input()
# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown

if name == 'dog':
    print('mammal')
elif name == 'crocodile' or name == 'tortoise' or name == 'snake':
    print('reptile')
else:
    print('unknown')