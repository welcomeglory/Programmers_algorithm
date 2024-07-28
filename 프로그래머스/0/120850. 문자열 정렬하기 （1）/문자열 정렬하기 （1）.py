def solution(my_string):
    # 숫자만 추출하여 리스트에 저장
    numbers = [int(char) for char in my_string if char.isdigit()]
    
    # 숫자 리스트를 오름차순으로 정렬
    numbers.sort()
    
    return numbers