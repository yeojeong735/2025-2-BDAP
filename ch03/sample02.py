myBook = 2002,'파이썬', 200

my_book = 2002, '파이썬', 200
my_book2 = (2002, '파이썬', 200)
print(type(my_book))
print(my_book)

print(type(my_book2))
print(my_book2)

year, title, size = my_book
print(year)
print(title)
print(size)

print('-'*20)
print(my_book[0])
print(my_book[1])

print('-'*20)
print(my_book2[-1])
print(my_book2[-2])

print(len(my_book))
print(myBook[len(myBook)-1])