def solution(arr, flag):
    X = []
    
    for i in range(len(arr)):
        if flag[i]:
            # arr[i]를 arr[i] × 2 번 추가
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            # arr[i]만큼 마지막 원소를 제거
            X = X[:-arr[i]]
    
    return X