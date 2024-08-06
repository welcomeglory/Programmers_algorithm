def solution(arr):
    import math
    
    # 현재 배열의 길이
    length = len(arr)
    
    # 배열의 길이가 2의 거듭제곱이 될 때까지 필요한 개수의 0을 추가
    # 2의 거듭제곱으로 맞추기 위한 최소 길이 찾기
    next_power_of_two = 2 ** math.ceil(math.log2(length))
    
    # 추가할 0의 개수
    zeros_to_add = next_power_of_two - length
    
    # 배열에 0 추가
    result = arr + [0] * zeros_to_add
    
    return result