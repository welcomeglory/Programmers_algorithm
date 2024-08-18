def solution(n):
    answer = n ** (1/2)
    return (answer+1)**2 if answer == int(answer) else -1
