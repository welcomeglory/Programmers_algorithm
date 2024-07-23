def solution(array):
    array.sort()
    middle_index = len(sorted(array)) // 2
    return array[middle_index]