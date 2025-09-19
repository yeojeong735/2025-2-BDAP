
your_book = [2002, '파이썬', 200, '1교시']
#               0       1     2       3

new_book = your_book

print(your_book)
print(new_book)

your_book[0] = 2025

print('-'*20)
print(your_book)
print(new_book)

new_book = your_book[:]
print('-'*20)
print(your_book)
print(new_book)

your_book[0] = 2026
print('-'*20)
print(your_book)
print(new_book)