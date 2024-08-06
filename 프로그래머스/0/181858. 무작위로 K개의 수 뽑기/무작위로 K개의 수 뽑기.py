def solution(arr, k):
    # 중복 방지를 위한 set
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
        if len(result) == k:
            break
    
    # 길이가 k에 미치지 못할 경우 -1로 채우기
    if len(result) < k:
        result.extend([-1] * (k - len(result)))
    
    return result