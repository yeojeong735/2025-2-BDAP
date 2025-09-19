
import random


scores = dict()
for i in range(11, 50 + 1):
    scores['S' + str(i)] = random.randrange(50, 100+1)
print(scores)

#40명 학생의 평균 점수를 구하시오.

avg = sum(scores.values()) / len(scores)
print(avg)

'''
40명 중 최고 득점을 한 학생과 점수를 출력하시오.
여러 명인 경우, 학번이 가장 빠른 한 명만 출력되도록 하시오.
'''

high_score = 0
high_student_id = ''

for student_id, score in scores.items():
    if score > high_score:
        high_score = score
        high_student_id = student_id

print(high_student_id)



