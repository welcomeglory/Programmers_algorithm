def solution(date1, date2):
    # date1과 date2의 연도, 월, 일 비교
    if date1[0] < date2[0]:  # 연도 비교
        return 1
    elif date1[0] > date2[0]:  # 연도 비교
        return 0
    else:
        if date1[1] < date2[1]:  # 월 비교
            return 1
        elif date1[1] > date2[1]:  # 월 비교
            return 0
        else:
            if date1[2] < date2[2]:  # 일 비교
                return 1
            else:
                return 0