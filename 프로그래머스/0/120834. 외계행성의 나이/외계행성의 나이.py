def solution(age):
    # 숫자와 알파벳의 매핑 정의
    num_to_char = {i: chr(ord('a') + i) for i in range(10)}
    
    # 나이를 문자열로 변환
    age_str = str(age)
    
    # 각 숫자를 알파벳으로 변환
    result = ''.join(num_to_char[int(digit)] for digit in age_str)
    
    return result
