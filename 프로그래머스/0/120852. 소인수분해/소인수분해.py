def solution(n):
    factors = []
    # 2부터 시작하여 n의 소인수를 찾습니다.
    # 2는 가장 작은 소수이므로 먼저 처리합니다.
    while n % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        n //= 2
    
    # 3부터 시작하여 홀수 소수들로 나누어가면서 소인수를 찾습니다.
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            if factor not in factors:
                factors.append(factor)
            n //= factor
        factor += 2
    
    # n이 1보다 크다면 그것도 소수입니다.
    if n > 1:
        factors.append(n)
    
    return factors