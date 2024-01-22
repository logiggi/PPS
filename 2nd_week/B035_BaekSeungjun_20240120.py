N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

cnt = cur = 0
idx = len(coin) - 1
while cur != K and idx >= 0:
    if coin[idx] <= K-cur:
        cnt += (K-cur) // coin[idx]
        cur += (K-cur) // coin[idx] * coin[idx]
    idx -= 1
    
print(cnt)