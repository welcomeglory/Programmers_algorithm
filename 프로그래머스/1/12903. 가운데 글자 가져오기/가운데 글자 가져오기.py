def solution(s):
    s_list = list(s)
    s_len = len(s_list)
    # return "".join(s_list[s_len//2] if s_len % 2 == 1 else s_list[s_len//2-1:s_len//2+1])
    return s[(len(s)-1)//2 : len(s)//2 + 1]
