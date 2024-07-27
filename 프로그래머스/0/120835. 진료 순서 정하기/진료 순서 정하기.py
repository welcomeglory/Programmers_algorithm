def solution(emergency):
    # 응급도의 순위를 매기기 위해, 응급도와 원래 인덱스를 함께 저장
    indexed_emergency = list(enumerate(emergency))
    
    # 응급도를 기준으로 내림차순 정렬
    sorted_emergency = sorted(indexed_emergency, key=lambda x: x[1], reverse=True)
    
    # 순위 배열을 만들기
    ranks = [0] * len(emergency)
    for rank, (index, _) in enumerate(sorted_emergency):
        ranks[index] = rank + 1
    
    return ranks
