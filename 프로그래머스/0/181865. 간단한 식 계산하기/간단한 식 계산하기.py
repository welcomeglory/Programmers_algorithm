def solution(binomial):
    lists = binomial.split()
    x = int(lists[0])
    y = int(lists[2])
    if lists[1] == '+':
        return x+y
    elif lists[1] == '-':
        return x-y
    else: 
        return x*y

     