from pathlib import Path

order_path = Path(__file__).with_name('order.txt')

lines = []

with order_path.open(encoding='utf-8') as f:
    for line in f:

        # map() 리스트의 각 요소에 함수를 한 번씩 적용
        #str() 문자열로 변환
        # 쉼표 기준으로 분리하고 각각의 공백 제거
        name, count, price = map(str.strip, line.split(','))
        # int() 정수형으로 변환
        count = int(count)
        price = int(price.rstrip('원'))
        # 잘못된 주문 데이터 제외
        #가격이 0보다 작은 경우 + 가격이 1000보다 큰 경우 + 개수가 0보다 작은 경우를 모두제거
        if price < 0 or price > 1000 or count < 0:
            continue
        # 정상 주문 데이터 저장
        lines.append([name, count, price])
        # 개수 × 가격을 total에 누적
        total = 0
        total += count * price
# 정상 주문 목록 출력
print(lines)

# 총 주문 금액 출력
print(f'총 가격: {total}원')



