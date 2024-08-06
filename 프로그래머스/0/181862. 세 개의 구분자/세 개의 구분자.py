def solution(myStr):
    # 문자열을 'a', 'b', 'c'로 분할
    parts = myStr.split('a')
    parts = [item for sublist in [part.split('b') for part in parts] for item in sublist]
    parts = [item for sublist in [part.split('c') for part in parts] for item in sublist]
    
    # 비어있는 문자열 요소를 제거
    result = [part for part in parts if part]
    
    # 결과가 비어 있다면 ["EMPTY"] 반환
    return result if result else ["EMPTY"]