def solution(numbers, direction):
    n = len(numbers)  # 배열의 길이

    if direction == "left":
        # 왼쪽 회전
        return numbers[1:] + [numbers[0]]
    elif direction == "right":
        # 오른쪽 회전
        return [numbers[-1]] + numbers[:-1]
    else:
        raise ValueError("direction must be either 'left' or 'right'")
