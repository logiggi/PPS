import sys
sys.setrecursionlimit(10**5)

n = int(input())

board = [[] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for i in range(n):
    given = input()
    for e in given:
        board[i].append(e)
        
val = ['R', 'G', 'B']

def is_valid(y, x):
    return y >= 0 and y < n and x >= 0 and x < n

def dfs(y, x, value):
    visited[y][x] = True
    
    for i in range(4):
        ddy = y + dy[i]
        ddx = x + dx[i]
        if is_valid(ddy, ddx) and not visited[ddy][ddx] and board[ddy][ddx] == value:
            dfs(ddy, ddx, value) 

ans1 = 0     
for v in val:
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == v:
                ans1 += 1
                dfs(i, j, v)
                
for i in range(n):
    for j in range(n):
        visited[i][j] = False
        if board[i][j] == 'G':
            board[i][j] = 'R'
            
ans2 = 0     
for v in val:
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == v:
                ans2 += 1
                dfs(i, j, v)
        
print(ans1, ans2)