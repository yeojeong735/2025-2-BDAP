
a = 10
b = '10'
#c = a + b <- 오류!
#print(c)


print('-----------')


from decimal import Decimal
# decimal 클래스 : 부동 소수점 오차 문제를 해결하기 위해 고안됨

a = 0.1
b = 0.2
c = a + b
print(c)

a1 = Decimal('0.1')
b1 = Decimal('0.2')
c1 = a1 + b1
print(c1)
print(type(c1))