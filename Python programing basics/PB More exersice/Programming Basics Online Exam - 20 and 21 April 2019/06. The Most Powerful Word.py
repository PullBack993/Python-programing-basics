import math
import sys
max_sum_letters = -sys.maxsize
winner = None

while True:
    name = input()
    sum_letters = 0
    list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'O', 'Y', 'I']

    if name == 'End of words':
        print(f'The most powerful word is {winner} - {max_sum_letters}')
        break

    for letter in name:
        sum_letters += ord(letter)

    if name[0] in list_of_vowels:
        sum_letters = sum_letters * len(name)
    else:
        sum_letters = math.floor(sum_letters / len(name))

    if sum_letters >= max_sum_letters:
        max_sum_letters = sum_letters
        winner = name