def solution(sides):
    a, b = sides  # 두 변의 길이
    
    # c의 가능한 범위를 계산
    min_side = abs(a - b) + 1
    max_side = a + b - 1
    
    # 가능한 변의 개수 계산
    if min_side > max_side:
        return 0
    else:
        return max_side - min_side + 1

# 예시 사용
print(solution([3, 4]))  # 출력: 5 (c는 2, 3, 4, 5, 6 중 하나일 수 있음)
