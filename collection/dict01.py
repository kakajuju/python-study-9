# 딕셔너리 key : value 세트로 저장
# {키:값}

lux = { 'healht':490, 'mana':334, 'melee':550, 'armor':18.72 }
print(lux)
print(type(lux))    # <class 'dict'>

# 리스트 값 찾기 리스트[인덱스]
# 딕셔너리 값 찾기 딕셔너리[키값]

person = { 'name':'홍길동','age':25, 'hobby':['독서', '운동'] }
print( person['name'] )
print( person['age'] )
print( person['hobby'] )
print( person['hobby'][1] )

d= { 'a':1, 'a':2 }
print(d)

# 딕셔너리의 키값   문자열, 숫자형, 튜플 가능 (리스트는 불가)

x = {1:'누구다', 2:'누구누구다', False:0, 3.5:[1,2], (1,2):'튜플의밸류'}
print(x)
print(x[1])
print(x[False])
print(x[3.5])
print(x[(1,2)])

# 빈 딕셔너리 만들기
a = {}
b = dict()
print(a, b)

# dict() 형태로 만들기
c = dict(health=340, mana=120)
d = dict(   [ ('health', 340),('mana', 120) ]   )
e = dict( zip( ['health', 'mana'], [340, 120] ) )

print(c)
print(d)
print(e)

# 값 변경 | 추가

# lux = { 'healht':490, 'mana':334, 'melee':550, 'armor':18.72 }
lux['health'] = 2490        #기존키값 변경
lux['mana_regen'] = 3.28    #신규로 추가
print(lux)

print(lux['mana'])
print(lux.get('mana'))

# print(lux['attack'])        # KeyError: 'attack'
print(lux.get('attack'))    # 존재하지 않으면 None
print(lux.get('attack', 50))

lux['attack'] = 81
print(lux.get('attack', 50))

# 키가 있는지 확인 in
print('health' in lux)
print('attack' in lux)
print('skills' in lux)

print(lux)
print(len(lux)) #개수

#삭제
del lux['attack']
print(lux)