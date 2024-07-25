def solution(arr, delete_list):
    delete_set = set(delete_list)  # delete_list를 집합으로 변환
    return [x for x in arr if x not in delete_set]  # delete_set에 없는 원소만 포함된 리스트 반환
