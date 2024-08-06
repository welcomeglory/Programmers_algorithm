def solution(a, b):
    # 홀수 여부를 체크하는 함수
    def is_odd(num):
        return num % 2 != 0
    
    # 두 숫자 모두 홀수인 경우
    if is_odd(a) and is_odd(b):
        return a**2 + b**2
    
    # 둘 중 하나만 홀수인 경우
    elif is_odd(a) or is_odd(b):
        return 2 * (a + b)
    
    # 둘 다 홀수가 아닌 경우
    else:
        return abs(a - b)