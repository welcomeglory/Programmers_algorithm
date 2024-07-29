def solution(n, t):
    num = n
    for i in range(1, t+1):
        num *= 2
    return num