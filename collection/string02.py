

s = 'Hello, World!'

# 문자 바꾸기 (대체하기) replace

print( s.replace('World','Good'))  # 원본 유지     비파괴적
print(s)

s = s.replace('World','Good')
print(s)

# 분리 / 합치기     split   join
words = 'apple kiwi banana melon'.split()
print(words)
print('apple kiwi banana melon'.split(','))

# 구분자.join(리스트)
print('-'.join(words))
print('/'.join(words))
print(''.join(words))

# 대소문자
print('hello'.upper())
print('GREAT'.lower())
print('hello great'.title())
print('hello great'.capitalize())

# 공백제거 (입력값 정리)
text = '  wonderful  '
print('[', text, ']')
print('[', text.strip(), ']')
print('[', text.lstrip(), ']')
print('[', text.rstrip(), ']')
print('[', '. this is text!! !'.strip('.!'), ']')   # 양쪽 끝에있는 지정한 문자를 정리

# 문자열 폭 정렬
print('[', 'python'.ljust(10), ']')
print('[', 'python'.rjust(10), ']')
print('[', 'python'.center(10), ']')
print('[', 'python'.zfill(10), ']')     # f  {2:0>5}
print( '2'.zfill(2) )

print('[', 'python'.ljust(10, '*'), ']')

# 문자 찾기
s = 'apple pineapple'
print( s.find('pl') )   # 앞에서부터 찾아서 가장먼저 찾은 위치
print( s.rfind('pl') )  # 오른쪽에서부터 찾기
print( s.find('ex') )   # 없으면 -1     if 찾은결과 == -1:  없구나~
print( s.index('pl') )  # 찾은 인덱스
# print( s.index('ex') )  # ValueError: substring not found   못찾으면 오류
print( s.count('p') )   #갯수세기

# 시작 끝 확인
file_name = 'report.xlsx'   #.xlsx  .png    .hwpx
print(file_name.startswith('report'))   #True
print(file_name.endswith('.xlsx'))      #True
print(file_name.endswith('.pptx'))      #False

# 문자 타입 종류 판단
#숫자확인
print( '1234'.isdigit() )
print( int('1234') )
print( '12q34'.isdigit() )  #False 숫자형태가 아님
# print( int('12q34') )   ValueError: invalid literal for int() with base 10: '12q34'
#문자확인
print( '1234'.isalpha() )
print( 'abcd'.isalpha() )
#숫자,영문만 True
print( 'abcd'.isalnum() )
print( '1234'.isalnum() )
print( '1234asd!@#'.isalnum() ) #비밀번호 검증에서 사용 가능

# 메소드 체이닝 (이어붙여서 수행)
raw = '  Hello, python  '

raw = raw.strip()
raw = raw.lower()
raw = raw.replace('python', 'world')

print(raw)

raw2 = '  Hello, python  '
raw2 = raw2.strip().lower().replace('python', 'world2')
print(raw2)

#입력 한번에 정리
email = input('이메일: ').strip().lower()   #공백제거, 소문자로
print(email)
# s = email.split("@")
# s[0]  s[1]
user_id, domain = email.split("@")
rpint(user_id, domain)