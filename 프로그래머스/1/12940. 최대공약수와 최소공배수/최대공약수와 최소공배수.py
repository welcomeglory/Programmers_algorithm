import math

def solution(n, m):
    def gcd(a, b):
        return math.gcd(a, b)
    
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    answer = [gcd(n, m), lcm(n, m)]
    return answer