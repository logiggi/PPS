def DFS(node):
    visited[node] = True
    dfs_answer.append(node)
    
    for e in adj_list[node]:
        if visited[e] == False:
            DFS(e)
            
def BFS(node):
    visited[node] = True
    bfs_answer.append(node)
    
    q = [node]
    while q:
        for e in adj_list[q.pop()]:
            if visited[e] == False:
                visited[e] = True
                bfs_answer.append(e)
                q.insert(0, e)

N, M , start = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
for i in range(1, len(adj_list)):
    adj_list[i].sort()
    
visited = [False for _ in range(N+1)]
dfs_answer = []
DFS(start)
for e in dfs_answer:
    print(e, end=' ')

print()
for i in range(N+1):
    visited[i] = False
bfs_answer = []
BFS(start)
for e in bfs_answer:
    print(e, end=' ')