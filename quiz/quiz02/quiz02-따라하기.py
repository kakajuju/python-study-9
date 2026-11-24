# 문제1)
# url = 'https://www.python.org/downloads'
# 위 문자열에서 슬라이스를 사용해 아래 값을 꺼내 출력하세요.
# - 'https'
# - 'www.python.org'
# - 'downloads'
'''
url = 'https://www.python.org/downloads'
print(url[0:5])     # 방법1 https
print(url[0:5:1])   # 방법2 https
print(url[:5])      # 방법3 https

print(url[8:22])      # www.python.org
print(url[23:])      # 방법1 downloads
print(url[-9:])      # 방법2 downloads
'''


# 문제2)
# n = [-32, 5, 2, -10, 55, 7, 9, 0]
# - 홀수 번째 인덱스(1, 3, 5 ...)의 요소만 출력하세요.
# - 마지막 3개 요소를 출력하세요.
# - 리스트를 거꾸로 뒤집어서 출력하세요.
'''
n = [-32, 5, 2, -10, 55, 7, 9, 0]

print( n[1:len(n):2] )  # 방법1 [5, -10, 7, 0]
print( n[1::2] )        # 방법2 [5, -10, 7, 0]

print( n[-3:] )     # 방법1 [7, 9, 0]
print( n[5:] )      # 방법2 [7, 9, 0]

print( n[::-1] )    # [0, 9, 7, 55, -10, 2, 5, -32]
'''


# 문제3)
# 날짜 문자열 '20261102' 를 입력 받아서 2026년 11월 02일 로 출력하세요.

# date = '20261102'  YYYY-MM-DD
'''
date = input('날짜를 입력 (YYYYMMDD) : ')
print(date)
print(date[:4])
print(date[4:6])
print(date[6:])
print(date[-2:])

print(f'{date[:4]}년 {date[4:6]}월 {date[6:]}일')
print(date[:4],'년 ', date[4:6],'월 ', date[6:],'일', sep='')
'''

# 문제4)
# year = (2021, 2022, 2023, 2024, 2025, 2026)
# population = (10249679, 10195318, 10143645, 9994195, 9886021, 9810000)
# 최근 3년간의 연도와 인구 수를 출력하세요. (음수 인덱스 사용)
'''
year = (2021, 2022, 2023, 2024, 2025, 2026)
population = (10249679, 10195318, 10143645, 9994195, 9886021, 9810000)

print(year[-3:])
print(population[-3:])
'''