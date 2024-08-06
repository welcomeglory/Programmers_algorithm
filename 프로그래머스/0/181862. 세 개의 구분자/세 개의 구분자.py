def solution(myStr):
    # 'a', 'b', 'c'를 공백으로 대체
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    
    # 공백을 기준으로 문자열을 분할하고 빈 배열일 경우 ["EMPTY"]를 반환
    return myStr.split() if myStr.split() else ["EMPTY"]