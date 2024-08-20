def solution(price, money, count):
    # 총 필요한 금액을 계산
    total_cost = price * (count * (count + 1)) // 2
    
    # 부족한 금액을 계산
    shortfall = total_cost - money
    
    # 부족한 금액이 0보다 작거나 같으면 0을 반환하고, 그렇지 않으면 부족한 금액을 반환
    return max(shortfall, 0)