def solution(n):
    x = 1
    while (6 * x) % n != 0:
        x += 1
    return x