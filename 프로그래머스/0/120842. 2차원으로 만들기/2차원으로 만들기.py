def solution(num_list, n):
    # num_list의 길이를 n으로 나누어 필요한 행의 개수를 구합니다
    rows = len(num_list) // n
        
    return [num_list[i * n:(i + 1) * n] for i in range(rows)]
