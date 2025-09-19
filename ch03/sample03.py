my_book = (2002, '파이썬', 200)

print(my_book[0])

year = my_book[0]
print(year)

year = 2025
print(year)

#my_book[0] = 2025 error!!
#ㄴ튜플은 값을 변경할 수 없다

your_book = [2002, '파이썬', 200]
print(your_book)
print(type(your_book))

year, title, size = your_book
print(year)
print(title)
print(size)

print('-'*20)
print(your_book[0])
print(your_book[1])
print(your_book[2])