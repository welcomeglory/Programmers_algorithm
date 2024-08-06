def solution(arr):
    stk = []
    
    for num in arr:
        if not stk:
            # 스택이 빈 경우, 현재 요소를 스택에 추가
            stk.append(num)
        elif stk[-1] == num:
            # 스택의 마지막 요소와 현재 요소가 같은 경우, 마지막 요소 제거
            stk.pop()
        else:
            # 스택의 마지막 요소와 현재 요소가 다른 경우, 현재 요소 추가
            stk.append(num)
    
    # 스택이 비어 있으면 [-1] 반환, 그렇지 않으면 스택 반환
    return stk if stk else [-1]