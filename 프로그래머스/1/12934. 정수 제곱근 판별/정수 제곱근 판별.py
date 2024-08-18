import math
def solution(n):
    answer = math.sqrt(n)
    return (answer+1)*(answer+1) if answer == int(answer) else -1