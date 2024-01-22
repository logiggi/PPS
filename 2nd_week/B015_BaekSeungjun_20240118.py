import sys
sys.setrecursionlimit(10**5)

n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
start = int(input()) - 1

answer = 0
def DFS(x):
    visited[x] = True
    global answer
    answer += 1
    
    dx1 = x + arr[x]
    dx2 = x - arr[x]
    if dx1 >= 0 and dx1 < n and visited[dx1] == False:
        DFS(dx1)
    if dx2 >= 0 and dx2 < n and visited[dx2] == False:
        DFS(dx2)

DFS(start)
print(answer)