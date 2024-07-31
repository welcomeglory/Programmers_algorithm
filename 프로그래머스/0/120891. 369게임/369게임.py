def solution(order):
    # 숫자를 문자열로 변환
    order_str = str(order)
    
    # 박수를 쳐야 하는 숫자
    clap_digits = ['3', '6', '9']
    
    # 박수를 쳐야 하는 횟수를 계산
    clap_count = sum(order_str.count(digit) for digit in clap_digits)
    
    return clap_count
