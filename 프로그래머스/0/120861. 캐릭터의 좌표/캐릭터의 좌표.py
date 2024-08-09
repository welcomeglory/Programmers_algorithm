def solution(keyinput, board):
    answer = [0,0]
    x_max = (board[0]-1)//2
    y_max = (board[1]-1)//2
    for i in keyinput:
        if i == "up":
            if answer[1] == y_max:pass
            else:answer[1] += 1
        elif i == "down":
            if answer[1] == y_max*-1:pass
            else:answer[1] -= 1
        elif i == "left":
            if answer[0] == x_max*-1:pass
            else:answer[0] -= 1
        elif i == "right":  
            if answer[0] == x_max:pass
            else:answer[0] += 1
    return answer