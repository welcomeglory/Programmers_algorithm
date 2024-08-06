def solution(rank, attendance):
    # 참여 가능한 학생과 그들의 등수를 추출
    eligible_students = [(i, rank[i]) for i in range(len(attendance)) if attendance[i]]
    
    # 등수를 기준으로 오름차순 정렬
    eligible_students.sort(key=lambda x: x[1])
    
    # 상위 3명 선발
    top3_students = eligible_students[:3]
    
    # 학생 인덱스 추출
    a = top3_students[0][0]
    b = top3_students[1][0]
    c = top3_students[2][0]
    
    # 최종 결과 계산
    result = 10000 * a + 100 * b + c
    
    return result