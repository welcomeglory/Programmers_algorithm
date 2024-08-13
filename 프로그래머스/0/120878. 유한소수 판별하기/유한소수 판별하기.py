def get_factors(n):
    factors = []
    div = 2
    while n > 1:
        if n % div == 0:
            factors.append(div)
            n //= div
        else:
            div += 1
    return factors

def solution(a, b):
    answer = 1
    for i in range(2, 1001):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i


    factors = get_factors(b)
    print(factors)

    if not all(x in [2,5] for x in factors):
        answer = 2

    return answer