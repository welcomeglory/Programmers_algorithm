def solution(my_string):
    # 중복 제거와 순서 유지를 위한 집합
    seen = set()
    # 결과를 담을 리스트
    result = []

    for char in my_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    # 리스트를 문자열로 변환하여 반환
    return ''.join(result)