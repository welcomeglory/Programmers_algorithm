def solution(array, height):
    answer = filter(lambda h: h > height, array)
    return len(list(answer))