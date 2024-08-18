def solution(arr, divisor):
    filtered = [num for num in arr if num % divisor == 0]
    
    if filtered:
        return sorted(filtered)
    else:
        return [-1]