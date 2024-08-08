def solution(i, j, k):
    k = str(k)  # k를 문자열로 변환
    count = 0
    
    # i부터 j까지 반복
    for num in range(i, j + 1):
        num_str = str(num)  # 숫자를 문자열로 변환
        count += num_str.count(k)  # 문자열에서 k의 등장 횟수를 더함

    return count