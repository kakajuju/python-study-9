
# [파이썬 퀴즈7 - 제어문 종합 : 업다운 숫자 맞추기 게임]


# 1 ~ 100 사이 랜덤 숫자를 하나 정하고
# 사용자가 숫자를 입력하면 'UP' / 'DOWN' 힌트를 주세요.
# 맞추면 몇 번 만에 맞췄는지 출력하고 종료합니다.

# +옵션1) 기회는 7번. 7번 안에 못 맞추면 정답을 알려주고 종료
# +옵션2) 1 ~ 100 범위를 벗어난 입력은 기회를 차감하지 않고 다시 입력 받기



import random

answer = random.randint(1,100)      # 1~100 사이 랜덤닶

# print(answer)   # 숫자 확인

count = 0

while True:

    #사용자가 숫자 입력
    num = int(input('숫자 입력 (1~100):'))

    # 정상범위를 벗어나면 필터링

    # if num < 1 or num > 100:  #방법 1)
    if not(1 <= num <= 100):    #방법 2)
        print('잘못입력하셨습니다 1~100 중에...')
        continue    #여기서 다시 처음부터


    #시도횟수 증가
    count += 1

    #정답에 맞는지, UP, DOWN 조건
    if num == answer:
        print(answer, '정답입니다!!')
        print(count, '회 만에 맞췄습니다!!')
        break # 정답이므로 종료
    elif num > answer:
        print('DOWN')
    elif num < answer:
        print('UP')

    if count == 7:  # +옵션1)
        print('기회 7번 모두 소진. 정답은 ', answer)
        break

    # 출력

    # 정답 -> 종료
    #틀리면 -> 돌아가서 입력부터 재시도