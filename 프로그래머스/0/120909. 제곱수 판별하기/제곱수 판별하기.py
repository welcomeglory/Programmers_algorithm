import math
def solution(n):
    num = int(math.sqrt(n))
    if num*num == n:
        return 1
    else:
        return 2
   
