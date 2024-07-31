def solution(myString, pat):
    # 가장 긴 부분 문자열은 myString에서 시작해서 pat로 끝나는 부분 문자열 중 하나입니다.
    # 따라서, myString의 마지막부터 거꾸로 탐색해서 pat로 끝나는 첫 번째 부분 문자열을 찾으면 됩니다.
    
    # 초기화: myString의 길이와 pat의 길이
    myString_len = len(myString)
    pat_len = len(pat)
    
    # pat이 myString의 마지막에 오는 경우를 찾아야 하므로 역순으로 탐색
    for i in range(myString_len - pat_len, -1, -1):
        # 부분 문자열을 가져옴
        sub_string = myString[i:i + pat_len]
        # 부분 문자열이 pat과 같다면, 해당 부분 문자열부터 myString의 끝까지가 답이 됨
        if sub_string == pat:
            return myString[:i + pat_len]

    # 모든 경우를 다 살펴도 return되지 않았다면, pat이 myString의 부분 문자열이 아니었다는 뜻 (제한사항에서 이 경우는 없음)
    return ""