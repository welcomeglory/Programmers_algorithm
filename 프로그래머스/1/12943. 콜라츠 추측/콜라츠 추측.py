def solution(num):
    # 초기값 검사
    if num == 1:
        return 0

    count = 0  # 반복 횟수를 기록할 변수
    
    # 최대 500번 반복
    while num != 1 and count < 500:
        if num % 2 == 0:
            num //= 2  # 짝수일 때 2로 나누기
        else:
            num = num * 3 + 1  # 홀수일 때 3을 곱하고 1 더하기
        
        count += 1  # 반복 횟수 증가
    
    # 결과 반환
    if num == 1:
        return count
    else:
        return -1
