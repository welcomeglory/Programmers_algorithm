def solution(s):
    # 문자열을 공백을 기준으로 분리
    elements = s.split()
    
    # 스택을 이용해 숫자를 관리
    stack = []
    
    for element in elements:
        if element == "Z":
            if stack:
                stack.pop()  # 가장 최근의 숫자를 제거
        else:
            stack.append(int(element))  # 숫자를 스택에 추가
    
    # 스택의 숫자들을 모두 더하여 결과 반환
    return sum(stack)