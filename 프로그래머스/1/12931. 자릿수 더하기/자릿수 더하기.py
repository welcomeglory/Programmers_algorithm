def solution(n):
    str_= list(str(n))
    sum = 0
    for i in range(len(str_)):
        sum += int(str_[i])
        
    return sum