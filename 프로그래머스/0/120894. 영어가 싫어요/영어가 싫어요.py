def solution(numbers):
       # 영어 숫자와 숫자를 매핑하는 딕셔너리
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    # 변환된 결과를 저장할 문자열
    result = ""
    
    # 현재 처리 중인 단어를 저장할 문자열
    word = ""
    
    # 입력 문자열을 한 글자씩 순회
    for char in numbers:
        word += char
        # 현재 word가 num_dict의 키 중 하나라면 변환
        if word in num_dict:
            result += num_dict[word]
            # 변환 후 word를 초기화
            word = ""
    
    # 최종 결과를 정수로 변환하여 반환
    return int(result)