# [파이썬 퀴즈4 - 조건문]

# 문제1)
# 나이를 입력 받아서 요금을 출력하세요.
# - 8세 미만 : 무료
# - 8 ~ 13세 : 650원
# - 14 ~ 18세 : 1050원
# - 19 ~ 64세 : 1350원
# - 65세 이상 : 무료
'''
age = int(input('나이 입력 : '))
if age < 8:
    print('무료')
elif age <= 13:
    print('650원')
elif age <= 18:
    print('1050원')
elif age <= 64:
    print('1350원')
else:
    print('무료')
'''

# 문제2)
# 년도를 입력 받아서 윤년인지 출력하세요.
# - 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년
# - 또는 400으로 나누어 떨어지면 윤년

# 윤년 = 2월이 29일까지 있는 해...
# %나머지연산 == 0
'''
year = int(input('년도입력 YYYY : '))

#방법 1)
if year % 400 == 0:
    print('윤년')
elif year % 100 == 0:
    print('윤년X')
elif year % 4 == 0:
    print('윤년')
else:
    print('윤년x')

#방법 2)
if year % 4 ==0:
    if year % 400 == 0:
        print('윤년')
    else:
        if year % 100 == 0:
            print('윤년X')
        else:
            print('윤년')
else:
    print('윤년x')

#방법 3)
#방법 3-1)
# if year % 4 ==0:
#     if year % 400 == 0:
#         실행문

# if year % 4 ==0 and year % 400 == 0:

#방법 3-2)
# if year % 400 == 0:
#     print('윤년')
# else (year % 4 == 0 and year % 100 != 0):
#     print('윤년')

# if year % 400 == 0 or (year % 4 == 0 and (not year % 100 == 0)):
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('윤년')
else:
    print('윤년x')
'''

# 문제3)
# 교통카드 잔액 9000원에서 나이에 따른 요금(문제1)을 차감하고
# 남은 잔액을 출력하세요.
'''
money = 9000        # 보유한 돈
age = int(input('나이 입력 : '))
#방법 1)
if age < 8:
    print('무료')
    print(money)
elif age <= 13:
    print('650원')
    print(money-650)
    money = money-650
elif age <= 18:
    print('1050원')
    money = money-1050
    print(money-1050)
elif age <= 64:
    print('1350원')
    money = money-1350
    print(money-1350)
else:
    print('무료')
    print(money-0)
print(money)

#방법 2)
fee = 0 # 요금 변수
if age < 8:
    fee =0
elif age <= 13:
    fee = 650
elif age <= 18:
    fee = 1050
elif age <= 64:
    fee = 1350
else:
    fee = 0

money = money - fee
print('요금', fee, '잔액',money)
'''

# 문제4)
# 세 정수를 공백으로 구분해 입력 받아서 가장 큰 수를 출력하세요. (max 함수 사용하지 않기)

a, b, c = map(int, input('정수 3개 (띄어쓰기구분) : ').split())
print(a,b,c)

#방법 1)
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

#방법 2)
big = a
if (b > big):
    big = b
if c > big:
    big = c

print(big)

#방법 3) - max를 사용해서
# print(max(a,b,c))

