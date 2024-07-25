def solution(numbers):
    numbers.sort()
    
    # 배열의 가장 큰 두 수를 곱한 값
    max1 = numbers[-1] * numbers[-2]
    
    # 배열의 가장 작은 두 수를 곱한 값 (음수가 있을 경우 유용함)
    min1 = numbers[0] * numbers[1]
    
    # 두 값 중 최대값을 반환
    return max(max1, min1)
