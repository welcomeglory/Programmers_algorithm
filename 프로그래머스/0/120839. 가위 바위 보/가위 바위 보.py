def solution(rsp):
    # 변환 사전 정의
    win_map = {
        '2': '0',  # 가위(2) → 바위(0)
        '0': '5',  # 바위(0) → 보(5)
        '5': '2'   # 보(5) → 가위(2)
    }
    
    return ''.join(win_map[char] for char in rsp)
