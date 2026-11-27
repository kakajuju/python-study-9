# [파이썬 퀴즈9 - 2차원 리스트]


scores = [
    ['김철수', 90, 85, 77],
    ['이영희', 72, 95, 88],
    ['박민수', 65, 70, 92],
    ['최지우', 98, 89, 94],
]
# (이름, 국어, 영어, 수학)


# 문제1)
# 학생별 총점과 평균을 출력하세요.
# 출력 예) 김철수 총점 252 평균 84.0

for x, y, z, a in scores:
    s = y+z+a
    print(f'{x} 총점 {s} 평균 {s/3}')


# 문제2)
# 과목별(국어, 영어, 수학) 평균을 출력하세요.

for i in scores:
    kor = [i[1] for i in scores]
    kor_avg = sum(kor) / len(scores)
    eng = (scores[0][2] + scores[1][2] + scores[2][2] + scores[3][2])
    mat = (scores[0][3] + scores[1][3] + scores[2][3] + scores[3][3])
print(f'국어 평균: {kor_avg}')
    print(f'영어 평균: {eng/4}')
    print(f'수학 평균: {mat/4}')

# 문제3)
# 총점이 가장 높은 학생의 이름을 출력하세요.



# 문제4)
# 3행 4열 2차원 리스트를 만들고 아래처럼 1부터 순서대로 채워서 출력하세요.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12