A = int(input())
B = int(input())
C = int(input())

res = str(A*B*C)

cnt = [0 for _ in range(10)]

for e in res:
    cnt[ord(e)-ord('0')] += 1
    
for e in cnt:
    print(e, end='\n')