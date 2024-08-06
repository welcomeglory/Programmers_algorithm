def solution(picture, k):
    # 확대된 그림을 담을 리스트
    enlarged_picture = []
    
    # 각 행을 k배 확대
    for row in picture:
        enlarged_row = ''.join([char * k for char in row])
        # 각 행을 k배 반복
        for _ in range(k):
            enlarged_picture.append(enlarged_row)
    
    return enlarged_picture