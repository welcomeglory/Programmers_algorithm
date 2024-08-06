def solution(myString):
    listed_str = list(myString)
    
    for i in range(len(myString)):
        if listed_str[i] < 'l':
            listed_str[i] = 'l'     
    
    return ''.join(listed_str)