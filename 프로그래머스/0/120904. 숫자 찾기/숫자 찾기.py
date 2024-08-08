def solution(num, k):
    listed_str = list(str(num))
    for i in range(len(listed_str)):
        if listed_str[i] == str(k):
            return i+1
    return -1
