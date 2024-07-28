def solution(n):
    # 초기값 설정
    i = 1
    factorial = 1
    
    # n의 범위 내에서 최대 팩토리얼 i를 찾기 위한 반복
    while True:
        # 현재 팩토리얼 값이 n을 초과하면 종료
        if factorial > n:
            return i - 1
        # 팩토리얼 계산을 계속 진행
        i += 1
        factorial *= i
    
    return i - 1  # 마지막으로 만족한 i값을 반환