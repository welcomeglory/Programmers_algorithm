def solution(s):
    # 문자열 s를 공백을 기준으로 분리하여 리스트로 변환
    numbers = list(map(int, s.split()))
    
    # 최소값과 최대값을 찾음
    min_val = min(numbers)
    max_val = max(numbers)
    
    # 결과를 형식에 맞게 문자열로 반환
    return f"{min_val} {max_val}"
