def solution(my_string):
    answer = 0 
    for char in my_string:
        if char.isdigit(): #문자가 숫자인지 확인
            answer += int(char)        
    return answer