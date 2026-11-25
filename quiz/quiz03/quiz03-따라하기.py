# [파이썬 퀴즈3 - 딕셔너리]
# 문제1)
# 아래 정보를 저장하는 딕셔너리 student 를 만드세요.
# 이름: 김파이, 학년: 2, 전공: 컴퓨터공학, 점수: [90, 85, 77]
# - 이름과 전공을 출력하세요.
# - 점수 중 두 번째 점수를 출력하세요.
# - 학년을 3으로 변경하고, 'email' 키에 'kim@py.com' 을 추가한 뒤 출력하세요.
'''
student = {'name':'김파이', 'grade':2, 'major':'컴퓨터공학', 'scores':[90, 85, 77]}
print(student['name'], student['major'])
print(student['scores'][1])
student['grade'] = 3
student['email'] = 'kim@py.com' # 키 추가
print(student)
'''

# 문제2)

# keys = ['alpha', 'bravo', 'charlie', 'delta']
# values = [10, 20, 30, 40]
# 두 리스트로 딕셔너리를 만들고 'delta' 의 값을 출력하세요.
keys = ['alpha', 'bravo', 'charlie', 'delta']
values = [10, 20, 30, 40]
# d = dict(zip(['alpha', 'bravo', 'charlie', 'delta'], [10, 20, 30, 40]))
# print(list(zip(keys,values)))
d = dict(zip(keys,values))
print(d['delta'])


# 문제3)

camille = {'health': 575.6, 'health_regen': 1.7, 'mana': 338.8,
           'mana_regen': 1.63, 'melee': 125, 'attack_damage': 60,
           'attack_speed': 0.625, 'armor': 26, 'magic_resistance': 32.1,
           'movement_speed': 340}
# 키 이름을 입력 받아서 해당 값을 출력하세요.
# 없는 키를 입력하면 '없는 항목' 이라고 출력하세요. (if 없이 get 사용)
inp = input('키값 입력 :')
print(camille.get(inp, '없는 항목'))
