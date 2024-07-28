def solution(box, n):
    # 상자의 각 방향에 배치 가능한 주사위의 수를 계산합니다.
    count_width = box[0] // n
    count_height = box[1] // n
    count_depth = box[2] // n
    
    # 총 들어갈 수 있는 주사위의 개수를 계산합니다.
    return count_width * count_height * count_depth

# 예시
print(solution([10, 8, 6], 3))  # 예시를 확인해보세요.
