def solution(n):
    if n == 0:
        return 0
    
    sum_of_divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:  # Avoid adding the square root twice when n is a perfect square
                sum_of_divisors += n // i
    
    return sum_of_divisors