def solution(numbers):
    # 전체 숫자 집합
    all_numbers = set(range(10))
    
    # 주어진 숫자 집합
    given_numbers = set(numbers)
    
    # 누락된 숫자 집합
    missing_numbers = all_numbers - given_numbers
    
    # 누락된 숫자의 합을 반환
    return sum(missing_numbers)