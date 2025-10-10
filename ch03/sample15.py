data = { # <- set (집합)
    'bgnde',
    'sj',
    'endde'
}

# 추가
data.add('title')
data.add('title')
print(data) # <- 집합은 중복을 허용하지 않기 때문에 title이 하나만 추가 됨

# 삭제
data.remove('sj')
print(data)

if 'sj' in data:
    data.remove('sj')

# discard 메서드 : set 자료형에서 사용되며, 특정 요소를 집합에서 제거하는 역할
data.discard('sj')

