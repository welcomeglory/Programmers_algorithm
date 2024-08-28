def solution(board, h, w):
    answer = -2 # 가로, 세로로 찾는 범위 안에 기준이 되는 칸도 있기 때문에 -1 두번 해줌.
    color = board[h][w] # 기준이 되는 좌표, 색

    # 인접한 옆칸들만 확인하면 되니, 탐색할 범위를 먼저 만들어놓음.
    find_h_range = [] #[탐색 시작 min, 탐색 종료 max] 순
    find_w_range = [] #[탐색 시작 min, 탐색 종료 max] 순

    # h min
    if h>0:
        find_h_range.append(h-1)
    else:
        find_h_range.append(h)

    # h max
    if h<len(board):
        find_h_range.append(h+2) # 아래 for문 list 범위 index에서 +1해주는 과정을 미리 처리
    elif h==6:
        find_h_range.append(h+1) # 만약 최대 범위인 7보다 1작다면 5,6,7까지만 확인하면 되니 1만 더해줌.
    else:
        find_h_range.append(h)

    #print(find_h_range)

    for line_h in board[find_h_range[0]:find_h_range[1]]:
        if line_h[w]==color:
            answer+=1

    # w min
    if w>0:
        find_w_range.append(w-1)
    else:
        find_w_range.append(w)

    # w max
    if w<len(board[0]):
        find_w_range.append(w+2)
    elif w==6:
        find_w_range.append(w+1)
    else:
        find_w_range.append(w)

    #print(find_w_range)

    for e in board[h][find_w_range[0]:find_w_range[1]]:
        if e==color:
            answer+=1

    return answer