
# [파이썬 퀴즈7 - 제어문 종합 : 업다운 숫자 맞추기 게임]


# 1 ~ 100 사이 랜덤 숫자를 하나 정하고
# 사용자가 숫자를 입력하면 'UP' / 'DOWN' 힌트를 주세요.
# 맞추면 몇 번 만에 맞췄는지 출력하고 종료합니다.
# +옵션1) 기회는 7번. 7번 안에 못 맞추면 정답을 알려주고 종료
# +옵션2) 1 ~ 100 범위를 벗어난 입력은 기회를 차감하지 않고 다시 입력 받기

# import random
# random.randint(1,100)

import random
r = ( random.randint(1,100) )
print(r)

count = int(input('횟수입력:'))

for i in range(1, 101):
    if count < r:
        print('UP')
    elif count > r:
        print('DOWN')
    else:
        print(r)


while True:
    count = input('숫자:')

    if count == random:
        break
    if cmd =='':
        continue #빈입력 무시
    print(random)