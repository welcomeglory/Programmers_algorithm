def solution(n):
    # n x n 배열 초기화
    spiral = [[0] * n for _ in range(n)]

    # 방향 벡터 (오른쪽, 아래쪽, 왼쪽, 위쪽)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 현재 위치와 방향
    row, col = 0, 0
    direction_index = 0
    
    for num in range(1, n * n + 1):
        spiral[row][col] = num
        
        # 다음 위치 계산
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        # 경계와 방문 확인
        if (0 <= next_row < n and 0 <= next_col < n and spiral[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            # 방향 변경
            direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]
    
    return spiral