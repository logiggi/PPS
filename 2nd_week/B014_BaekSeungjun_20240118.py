import sys
sys.setrecursionlimit(10**5)

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

board = [[0 for _ in range(51)] for _ in range(51)]
visited = [[False for _ in range(51)] for _ in range(51)]

def is_valid(y, x, w, h):
    return y >= 0 and y < h and x >= 0 and x < w

def DFS(y, x, w, h):
    visited[y][x] = True
    
    for i in range(8):
        ddy = y + dy[i]
        ddx = x + dx[i]
        if is_valid(ddy, ddx, w, h) and visited[ddy][ddx] == False and board[ddy][ddx]:
            DFS(ddy, ddx, w, h)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    for i in range(h):
        given = list(map(int, input().split()))
        for j in range(w):
            visited[i][j] = False
            board[i][j] = 0
            board[i][j] = given[j]
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and board[i][j]:
                answer += 1
                DFS(i, j, w, h)
                
    print(answer)