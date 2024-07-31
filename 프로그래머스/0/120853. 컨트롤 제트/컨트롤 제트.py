def solution(s):
    return sum( map(int, [i for i in list(s.replace(" Z","Z").split(' ')) if "Z" not in i])) 