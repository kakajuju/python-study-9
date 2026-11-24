
# 큰따옴표 작은따옴표
hello = 'Hello, World!'
hi = "안뇽하세요"

print(hello)
print(hi)
print(type(hi))

s1 = "my name's ..."
s2 = 'hi"hello"'
s3 = '큰"따옴표 작은\' \"따옴표'        #\' 이스케이프문자      \n : 줄바꿈
print(s1)
print(s2)
print(s3)

#여러줄 문자열
s4 = '''
    여러줄
    문자열을
    나타낼때
    사용할수 있다.
'''
print(s4)

'''
이거 사용을
여러줄 주석처럼
사용도 가능
'''

s5 = """
    여러줄
    문자열을
    나타낼때 "큰따옴표도 가능
    사용할수 있다.
"""
print(s5)

#이스케이프 문자
print('줄바꿈\n문자')
print('탭 띄어쓰기\t문자')
print('역슬래시 \\ \\ 문자')

# 문자열 연산
a = "hello"
b = "World"

print(a + b)
print(a + ' ' + b)
print(a, b, sep=' ')
print( a * 3 )  #반복의미
print( '-' * 30 )   #구분선 역할

#문자함수
print(len(a))
print(len('글자길이찾아봐라'))
print('ll' in a)
print('ll' in b)
print('ll' not in b)

num = '123'
print( int(num) + 123 )
print( str(123) + '456' )