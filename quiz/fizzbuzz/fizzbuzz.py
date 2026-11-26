# FizzBuzz 문제
# 1 ~ 100 까지 출력하면서
# 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 공배수는 FizzBuzz 출력
'''
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
'''

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)