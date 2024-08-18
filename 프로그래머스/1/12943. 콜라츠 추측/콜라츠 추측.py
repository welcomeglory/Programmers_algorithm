def solution(num):
    return (lambda c: c if c < 500 and num == 1 else -1)(len([num for _ in range(500) if num != 1 and (num := num // 2 if num % 2 == 0 else num * 3 + 1)]))
