book_name = input()

counter = 0
current_book = input()
while current_book != 'No More Books':
    if current_book == book_name:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1
    current_book = input()

if current_book == 'No More Books':
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')


searched_book = input()
book_count = 0
current_books = input()
while current_book != searched_book:
    if current_book == 'No More Books':
        break
    book_count += 1
    current_book = input()

if current_book == 'No More Books':
    print(f'the book')
    print(f'you chek')
else:
    print(f'you checked books and found')