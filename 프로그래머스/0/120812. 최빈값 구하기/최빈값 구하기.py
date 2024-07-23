from collections import Counter

def solution(array):
    # 1. 배열의 빈도를 계산
    counter = Counter(array)
    
    # 2. 최빈값 찾기
    max_freq = max(counter.values())
    
    # 3. 최빈값이 여러 개인지 확인
    modes = [key for key, value in counter.items() if value == max_freq]
    
    # 4. 최빈값이 하나면 그 값을 반환, 그렇지 않으면 -1 반환
    if len(modes) == 1:
        return modes[0]
    else:
        return -1