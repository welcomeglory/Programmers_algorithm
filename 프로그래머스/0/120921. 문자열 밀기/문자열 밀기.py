import re
def solution(A, B):
    return (B*2).index(A) if re.search(A,B*2) else -1