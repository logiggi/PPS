cnt = 0
def DFS(node):
    global cnt
    visited[node] = True
    
    for e in adj_list[node]:
        if visited[e] == False:
            DFS(e)
            cnt += 1    
            
# def BFS(node):
#     global cnt
#     visited[node] = True
#     q = [node]
#     while q:
#         for e in adj_list[q.pop()]:
#             if visited[e] == False:
#                 visited[e] = True
#                 q.insert(0, e)
#                 cnt += 1

N = int(input())
edge_num = int(input())

adj_list = [[] for _ in range(N+1)]
for i in range(edge_num):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
visited = [False for _ in range(N+1)]
DFS(1)
print(cnt)