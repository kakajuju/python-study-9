# 리스트 조작


a = [30,20,50,60,10]

for i in range(len(a)):
    print(a[i], end=' ')
print()

for v in a:
    print(v, end=' ')
print()

for idx, value in enumerate(a):
    print(idx, value)

i = 0
while i < len(a):
    print(a[i], end=' ')
    i = i + 1
print()


# 최소값, 최대값

# 최소값
smallest = a[0]
for v in a:
    if v <= smallest:
        smallest = v
print('최소값', smallest)

# 최대값
largest = a[0]
for v in a:
    if v >= largest:
        largest = v
print('최소값', largest)

# 함수 min최소값 max최대값 sum합
print(min(a), max(a), sum(a))
# 평균   총합   / 갯수
print( sum(a) / len(a) )


# 리스트 표현식 (리스트 컴프리핸션)
# [식 for 변수 in 반복이가능한객체]

b = [i for i in range(10)]
print(b)
#아래와 같다.
b = []
for i in range(10):
    b.append(i)
print(b)


c = [i*10 for i in range(1, 11)]
print(c)
#아래와 같다.
c = []
for i in range(1, 11):
    c.append(i*10)
print()

# 조건붙이기 추가
# [식 for 변수 in 반복이가능한객체 if 조건]
d = [i for i in range(10) if i % 2 == 0]
print(d)
#아래와 같다.
d = []
for i in range(10):
    if i%2 == 0:
        d.append(i)
print(d)


e = [ x+5 for x in range(10) if x%2 == 1 ]
print(e)

# 문자열 리스트
words = ['apple', 'banana', 'kiwi']

#upper 대문자로     lower 소문자로
print( words[0].upper() )

words_upper = [ v.upper() for v in words ]
print(words_upper)  # ['APPLE', 'BANANA', 'KIWI']

# 문자길이
words_len = [ len(v) for v in words ]
print(words_len)    # [5, 6, 4]

# map 모든 요소들에게 같은 함수 적용
words_len2 = list(map(len, words))
print(words_len2)

a = [1.1, 2.2, 3.3, 4.4]
b = list(map(int, a))       #실수형숫자 int(1.1) -> 1
print(b)

nums = list(map(str, range(5))) # 모두 문자로 바꾸겟다~
nums2 = list(range(5))
print(nums)
print(nums2)


# 입력값 split --> map 적용
x = list(map(int, input('숫자 여러개 띄어쓰기로 입력:').split()))
print(x)


# 튜플 -> 값이 바뀌지 않는다.
t = (30, 20, 50, 60, 10 ,40)
print(t.count(50), t.index(30))
print(min(t), max(t), sum(t))
t_even = tuple( i for i in range(10) if i%2 == 0)
print(t_even)