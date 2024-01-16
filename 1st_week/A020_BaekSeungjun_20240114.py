cur = 0
answer = 0
while True:
    a, b = map(int, input().split())
    
    cur -= a
    cur += b
    answer = max(cur, answer)
    
    if b == 0:
        break

print(answer)