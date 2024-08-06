def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    if rows > cols:
        # 열의 수를 행의 수에 맞추기 위해 각 행의 끝에 0을 추가
        for row in arr:
            row.extend([0] * (rows - cols))
        # 추가된 열을 갖는 배열을 리턴
        return arr
    elif cols > rows:
        # 각 행의 길이를 맞추고, 부족한 행을 0으로 채운 행으로 추가
        # 행 길이를 맞추기
        new_arr = [row + [0] * (cols - len(row)) for row in arr]
        # 부족한 행 추가
        new_arr.extend([[0] * cols for _ in range(cols - rows)])
        return new_arr
    
    # 행과 열의 수가 같은 경우 원본 배열을 그대로 리턴
    return arr