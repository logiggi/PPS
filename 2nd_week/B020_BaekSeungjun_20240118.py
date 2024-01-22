dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

board = []
is_empty = [True for _ in range(999999+1)]
res = []
answer = 0

def is_valid(y, x):
    return y >= 0 and y < 5 and x >= 0 and x < 5

def DFS(y, x):
    if len(res) == 6:
        global answer
        num = 0
        for e in res:
            num = (num + e) * 10
        num //= 10
        if is_empty[num]:
            is_empty[num] = False
            answer += 1
        return
    
    for i in range(4):
        ddy = y + dy[i]
        ddx = x + dx[i]
        
        if is_valid(ddy, ddx):
            res.append(board[ddy][ddx])
            DFS(ddy, ddx)
            res.pop()
        
for _ in range(5):
    board.append(list(map(int, input().split())))
    
for i in range(5):
    for j in range(5):
        DFS(i, j)
        
print(answer)