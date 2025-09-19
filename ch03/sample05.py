my_book = (2002, '파이썬', 200, '1교시')
your_book = [2002, '파이썬', 200, '1교시']
#               0       1     2       3

other_book = your_book
new_book = your_book[1:3]

print('new:', new_book)
print('other:', other_book)
print('my:', my_book)

print(id(my_book), id(new_book), id(other_book))
other_book[0] = 2025
print('your:', your_book)
print('other:', other_book)
print('my:', my_book)

#sample13.py