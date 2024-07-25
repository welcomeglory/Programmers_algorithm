def solution(my_string, letter):
    answer = ''
    chars = list(my_string)
    for n in chars:
        if n != letter:
            answer += n    
    return answer