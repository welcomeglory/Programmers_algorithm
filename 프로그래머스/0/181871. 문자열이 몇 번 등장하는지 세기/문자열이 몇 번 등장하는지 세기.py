def solution(myString, pat):
    count = 0
    start = 0
    while start <= len(myString) - len(pat):
        pos = myString.find(pat, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count
