def solution(s):
    from collections import Counter
    
    # 문자의 빈도수 계산
    freq = Counter(s)
    
    # 한 번만 등장하는 문자 추출
    unique_chars = [char for char, count in freq.items() if count == 1]
    
    # 한 번만 등장하는 문자 사전 순 정렬
    unique_chars.sort()
    
    # 결과 문자열 생성
    return ''.join(unique_chars)