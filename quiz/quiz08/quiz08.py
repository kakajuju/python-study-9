# [파이썬 퀴즈8 - 리스트]


# 문제1)
# scores = [88, 92, 75, 64, 95, 81, 70]
# - 최고점, 최저점, 평균을 출력하세요.
# - 80점 이상인 점수만 모은 리스트를 만들어 출력하세요. (for 와 리스트 표현식 두 가지 방법)
# - 점수를 높은 순서로 정렬한 새 리스트를 출력하세요. (원본 유지)

scores = [88, 92, 75, 64, 95, 81, 70]
# - 최고점, 최저점, 평균을 출력하세요.
print(max(scores), min(scores), sum(scores) / len(scores))

# - 80점 이상인 점수만 모은 리스트를 만들어 출력하세요. (for 와 리스트 표현식 두 가지 방법)
#for 표현식
num = []
for i in scores:
    if i >= 80:
        num.append(i)
print(num)
# 리스트 표현식
num = [i for i in scores if i >= 80]
print(num)

# - 점수를 높은 순서로 정렬한 새 리스트를 출력하세요. (원본 유지)
e = sorted(scores, reverse=True)
print(e)


# 문제2)
# 공백으로 구분된 단어들을 입력 받아서
# - 단어 개수
# - 가장 긴 단어
# - 길이가 5 이상인 단어만 대문자로 바꾼 리스트
# 를 출력하세요.
word = list(map(str, input('공백으로 구분된 단어들을 입력:').split())) # make go important very people
print(word) # ['make', 'go', 'important', 'very', 'people']

# - 단어 개수
words_len = [ len(v) for v in word ]    # 요소 v
print(words_len)    # [4, 2, 9, 4, 6]

# - 가장 긴 단어
print(max(word, key=len)) # important

# - 길이가 5 이상인 단어만 대문자로 바꾼 리스트
min_len = 5
big_len = [v.upper() for v in word if len(v) >= min_len ]
# for v in word (재료 꺼내기): word 리스트에서 단어를 하나씩 꺼내 v라고 부릅니다.
# if len(v) >= min_len (걸러내기): 꺼낸 단어 v의 길이가 5 이상인지 검사합니다. (5 미만이면 여기서 탈락합니다.)
# v.upper() (가공해서 담기): 검사를 통과한 단어 v를 대문자로 바꾼 뒤, 대괄호 [ ]로 감싸진 새 리스트에 담습니다
print(big_len) # ['IMPORTANT', 'PEOPLE']


# 문제3)
# 장바구니 프로그램
# cart = []
# 'add 상품명' 을 입력하면 추가, 'del 상품명' 을 입력하면 삭제, 'q' 입력시 종료
# 종료할 때 장바구니 목록을 번호와 함께 출력하세요.

# +옵션1) 이미 있는 상품을 add 하면 '이미 담긴 상품' 출력
# +옵션2) 없는 상품을 del 하면 '없는 상품' 출력

cart = []

while True:

    #사용자가 숫자 입력
    market = int(input('add 상품명 : 추가, del 상품명 : 삭제, q 입력 : 종료:'))

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