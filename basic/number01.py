
# 숫자 정수형 (int) 실수형 (float) 연산자

# 사칙연산

print( 1+1 )
print( 5-2 )
print( 3*4 )
print( 7/2 )    # 3.5 실수형
print( 4/2 )    # 2.0 실수형

# 몫 나머지
print( 7 // 2 )   # 나눗셈 몫 -> 3
print( 7 % 2 )  #나머지     -> 1

print( divmod(7,2))     # (3, 1) ( 몫, 나머지)

# 거듭제곱
print(2 ** 5) # 2의 5제곱 : 2*2*2*2*2

# 자료형 확인 : type()
print( type(10) )        #<class 'int'> 정수형
print( type(3.5) )       #<class 'float'> 실수형
print( type(4/2) )       #<class 'float'> 실수형
print( type(4//2) )      #<class 'int'> 정수형

# 정수 <-> 실수 변환
print( int(3.5) )   #정수형으로 변환 & 소수점 아래 버림
print( float(5) )   #실수형으로 변환
# print('100' + 1)  파이썬에서 문자열 + 숫자 계산 X
print(int('100') + 1)
print('100' + str(1)) # str 문자열 형태로 변환

# 실수 계산
print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3)
print(round(0.1 + 0.2, 2))  #round 반올림 함수

# 계산 우선순위
print (3+5*2)   # 3 + 10 = 13
print ((3+5)*2) # 8 *  2 = 16

# 숫자 표기, 큰 수 계산
print(123456789*87654321)
print(1000000)
print(1_000_000)    # _ 숫자 가독성 측면으로 사용하는 구분자
print(1,000,000)
print(10, 20, 30)