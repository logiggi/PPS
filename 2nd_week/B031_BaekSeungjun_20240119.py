def is_valid(node):
    return node >= 1 and node < 1000
        
start, end = map(int, input().split())
answer = abs(start-end)

n = int(input())
for i in range(n):
    favorite = int(input())
    answer = min(answer, abs(favorite-end)+1)

print(answer)