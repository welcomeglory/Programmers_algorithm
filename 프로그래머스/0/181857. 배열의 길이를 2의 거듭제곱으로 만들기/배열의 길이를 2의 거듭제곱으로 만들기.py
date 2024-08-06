import math

def solution(arr):
    
    n = math.log2(len(arr))

    if n.is_integer():
        return arr
    else:
        n = math.ceil(n)
        for i in range(len(arr), 2**n):
            arr.append(0)
        return arr
    
    
