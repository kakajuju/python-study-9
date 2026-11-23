
print('basic01.py')

# 1. 주석

#주석
# 앞에 #을 붙이면 그 라인은 주석

# 여러줄 주석
'''
이렇게 사용하면
여러줄 주석으로
사용할 수 있다.
'''

print('Hello') # 뒤에 샾부터 다시 주석

# 2. 세미콜론
# 세미콜론 안붙여도 오류나지 않음
print('Hello01')
print('Hello02')
print('Hello03')
print('Hello04'); print('Hello05') # 한줄에 여러문장 사용시에 ; 사용

# 3. 들여쓰기
# 구역 번위를 나타낼때 사용하던 {} 대신에 들여쓰기를 사용
# 들여쓰기 Tab 눌러서 적용 (공백 4칸)

print('들여쓰기')
# print('들여쓰기2') # IndentationError: unexpected indent <- 들여쓰기 문제 / 의미없이 들여쓰기 X

x= 10
print(x)
if x == 10:
    print('x는 10')
    print('들여쓰기 내부 범위')
    # if 문 내부에 속한 코드 블록

print('여기는 if문 밖...')

# 4. 코드 블록
if x > 5:
    print('5보다 크다')
    if x > 8:
        print('8보다 크다')
    print('x>5 블록')

if x > 100:     #if문 블록안에 아무것도 없으면 에러
    pass        # pass 키워드로 자리 채워두기

print('if문 다음')