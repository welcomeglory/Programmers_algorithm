def solution(order):
    # 가격 정의
    price_map = {
        'americano': 4500,
        'cafelatte': 5000
    }
    
    # 변환된 가격을 저장할 리스트
    prices = []

    for item in order:
        # 'anything'은 'americano'으로 변환
        if item == 'anything':
            item = 'americano'
        
        # 'ice' 또는 'hot'이 포함된 문자열 처리
        item = item.replace('ice', '').replace('hot', '')

        # 가격을 가져와 리스트에 추가
        price = price_map.get(item, 0)
        prices.append(price)
    
    # 총 합계 계산
    total_price = sum(prices)
    
    return total_price