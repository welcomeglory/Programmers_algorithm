import math
def solution(n):
    answer = math.sqrt(n)
    return (answer+1)**2 if answer == int(answer) else -1