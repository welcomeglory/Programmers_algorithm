def solution(numlist, n):
        return list(map(lambda x: x[1], sorted(map(lambda x: [abs(n - x), x], numlist), key=lambda x: [x[0], -x[1]])))

