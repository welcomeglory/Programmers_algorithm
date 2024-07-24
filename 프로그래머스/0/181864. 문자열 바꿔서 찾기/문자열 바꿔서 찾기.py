def solution(myString, pat):
     # 1. 'A'와 'B'를 서로 교환하여 새로운 문자열 생성
    transformed_string = ''.join('B' 
                                 if char == 'A' 
                                 else 'A' 
                                 for char in myString)
    if pat in transformed_string:
        return 1
    else:
        return 0