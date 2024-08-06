def solution(strArr):
    from collections import defaultdict
    
    # 길이별 문자열 개수를 저장할 딕셔너리
    length_count = defaultdict(int)
    
    # 문자열의 길이에 따라 개수 세기
    for s in strArr:
        length = len(s)
        length_count[length] += 1
    
    # 가장 많이 포함된 그룹의 크기 찾기
    max_group_size = max(length_count.values())
    
    return max_group_size