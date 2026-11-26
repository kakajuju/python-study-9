# [파이썬 퀴즈6 - 별찍기]


# 높이를 입력 받아서 아래 모양을 각각 출력하세요. (높이 5 예시)


# 문제1) 역삼각형
# *****
# ****
# ***
# **
# *
'''
for i in range(5):              
    for j in range(5):          
        if j > 4 - i :          
            print(" ", end="")
        else:
            print("*", end="")
    print()
print()
'''


# 문제2) 피라미드
#     *
#    ***
#   *****
#  *******
# *********
'''
for i in range(5):                  
    for j in range(5):          
        if j < 4 - i :          
            print(" ", end="")
        else:
            print("*", end="")           
    for k in range(5):          
        if k < i:
            print('*', end="")
    print()
print()
'''

# 문제3) 역피라미드 (문제2 를 뒤집은 모양)
# *********
#  *******
#   *****
#    ***
#     *
'''
for i in range(5):                  
    for j in range(5):          
        if j > i - 1 :          
            print("*", end="")
        else:
            print(" ", end="")           
    for k in range(5):          
        if k > i:
            print('*', end="")
    print()
print()
'''



# 문제4) 다이아몬드 (문제2 + 문제3, 가운데 줄은 한 번만)
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
