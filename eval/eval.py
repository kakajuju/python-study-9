from pathlib import Path

order_path = Path(__file__).with_name('order.txt')

lines = []

with order_path.open(encoding='utf-8') as f:
    for line in f:

        # map() 리스트의 각 요소에 함수를 한 번씩 적용
        #str() 문자열로 변환
        name, count, price = map(str.strip, line.split(','))
        count = int(count)
        price = int(price.rstrip('원'))
        if price < 0 or price > 1000 or count < 0:
            continue
        lines.append([name, count, price])
print(lines)

#가격이 0보다 작은 경우
#가격이 1000보다 큰 경우
#개수가 0보다 작은 경우
#제거
