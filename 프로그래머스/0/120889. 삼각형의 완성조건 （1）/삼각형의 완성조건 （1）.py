def solution(sides):
    s_sides=sorted(sides)
    if s_sides[2] >= s_sides[0]+s_sides[1]:
        return 2
    else:
        return 1