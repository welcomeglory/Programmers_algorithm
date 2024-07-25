def solution(myString):
    parts = myString.split('x')
    answer = [len(part) for part in parts]
    return answer