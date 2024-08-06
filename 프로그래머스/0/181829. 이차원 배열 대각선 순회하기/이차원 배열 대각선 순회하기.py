def solution(board, k):
    tmp = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i + j) <= k:
               tmp += board[i][j] 
    return tmp