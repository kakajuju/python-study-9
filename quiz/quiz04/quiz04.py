# [파이썬 퀴즈4 - 조건문]

# 문제1)
# 나이를 입력 받아서 요금을 출력하세요.
# - 8세 미만 : 무료
# - 8 ~ 13세 : 650원
# - 14 ~ 18세 : 1050원
# - 19 ~ 64세 : 1350원
# - 65세 이상 : 무료
age = int(input('나이를 입력하세요 : '))

if 8 <= age <= 13:
    print('650원')
elif 14 <= age <= 18:
    print('1050원')
elif 19 <= age <= 64:
    print('1350원')
else:
    print('무료')


# 문제2)
# 년도를 입력 받아서 윤년인지 출력하세요.
# - 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년
# - 또는 400으로 나누어 떨어지면 윤년
year = int(input('년도입력 YYYY : '))

if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print('윤년')
else:
    print('평년')


# 문제3)
# 교통카드 잔액 9000원에서 나이에 따른 요금(문제1)을 차감하고
# 남은 잔액을 출력하세요.
money = 9000
if 8 <= age <= 13:
    print(money-650)
elif 14 <= age <= 18:
    print(money-1050)
elif 19 <= age <= 64:
    print(money-1350)
else:
    print(money)



# 문제4)
# 세 정수를 공백으로 구분해 입력 받아서 가장 큰 수를 출력하세요. (max 함수 사용하지 않기)
a, b, c = map(int, input('정수 입력 : ').split())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)