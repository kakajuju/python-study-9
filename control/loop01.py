# 중첩 반복문

#if 조건:
#   if 조건:

for i in range(3):
    for j in range(4):
        print(i, j)

print()

for i in range(3):
    for j in range(4):
        print(i)
print()

for i in range(3):
    for j in range(4):
        print(j)
print()


for _ in range(5):
    print('★', end='')
print()

for i in range(5):          # 행 →
    for j in range(5):      # 열 ↓
        print('*', end='')
    print()
print()

for i in range(3):          # 행 →
    for j in range(10):      # 열 ↓
        print('*', end='')
    print()
print()

for i in range(3):
    print('*' * 10)
print()

for i in range(5):              # 0             1             ...     4 
    for j in range(5):          # 0 1 2 3 4     0 1 2 3 4     ...     0 1 2 3 4 
        if j <= i:
            print('*', end="")
    print()
print()

# 횟수 1 2 3 4 5번

for i in range(5):  # i : 0 1 2 3 4  -> i + 1 ->  횟수: 1 2 3 4 5      
    print( "*" * (i+1) )
print()


for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()


for i in range(5):              # 0             1             ...      4        
    for j in range(5):          # 0 1 2 3 4     0 1 2 3 4     ...      0 1 2 3 4
        if j < 4 - i :          # j < 4-0(i)     j < 4-1(4-i)         j < 0 (4-4) 
            print(" ", end="")
        else:
            print("*", end="")
    print()
print()


# 중첩 반복문 구구단
# 2단 ~ 9단     *1 ~ *9
# 2단일 때               3                      ...
# 1 2 3 4 5 6 7 8 9     1 2 3 4 5 6 7 8 9      ...

for x in range(2, 10):       # 2단부터 9단 까지
    print(x, '단')
    for y in range(1, 10):   # 1부터 9 까지
        print(f'{x} x {y} = {x*y}')
    print('-'*10)
print()