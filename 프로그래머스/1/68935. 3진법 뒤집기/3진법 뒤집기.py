# def solution(n):
#     if n == 0:
#         return 0
#     a = []
#     while n>3:
#         a.append(str(n%3))
#         n = n//3  
#     a.append(str(n))
#     return int(''.join(a),3)
def solution(n):
    # 1. 10진수를 3진수로 변환
    def decimal_to_base3(n):
        if n == 0:
            return '0'
        
        base3 = []
        while n > 0:
            base3.append(str(n % 3))
            n = n // 3
        
        base3.reverse()
        return ''.join(base3)

    # 2. 3진수 문자열을 뒤집음
    base3_str = decimal_to_base3(n)
    reversed_base3_str = base3_str[::-1]

    # 3. 뒤집힌 3진수 문자열을 10진수로 변환
    def base3_to_decimal(base3_str):
        return int(base3_str, 3)

    return base3_to_decimal(reversed_base3_str)
