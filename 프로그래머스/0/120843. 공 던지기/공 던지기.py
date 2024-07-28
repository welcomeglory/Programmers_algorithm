def solution(numbers, k):
    n = len(numbers)
    current_index = 0  # 공을 던지기 시작할 사람의 인덱스는 0입니다.
    
    # k번 공을 던질 때까지 반복
    for _ in range(k - 1):
        current_index = (current_index + 2) % n
    
    return numbers[current_index]

# 예시
print(solution([1, 2, 3, 4, 5], 3))  # 예시를 확인해보세요.
