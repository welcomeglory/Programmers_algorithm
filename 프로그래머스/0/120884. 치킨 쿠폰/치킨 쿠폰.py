def solution(chicken):
    service_chickens = 0  # 총 서비스 치킨 수
    coupons = chicken  # 초기 쿠폰 수는 시켜먹은 치킨 수와 동일

    while coupons >= 10:
        new_service_chickens = coupons // 10  # 새로 받는 서비스 치킨 수
        service_chickens += new_service_chickens  # 서비스 치킨 추가
        coupons = coupons % 10 + new_service_chickens  # 남은 쿠폰 및 새로 발급받은 쿠폰

    return service_chickens