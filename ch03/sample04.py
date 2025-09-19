your_book = [2002, '파이썬', 200]
print(your_book)
print(type(your_book))

#기존 데이터 변경
your_book[0] = 2025
print(your_book)

#추가도 가능
your_book.append('파이썬 프로그래밍')
print(your_book)

your_book.insert(1,'프로그래밍 과목')

#삭제
your_book.remove('파이썬')
print(your_book)