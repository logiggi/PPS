f = [0 for i in range(10000)]

N = int(input())
f[1] = 1
f[2] = 1
for i in range(3, N+1):
    f[i] = f[i-1] + f[i-2]
    
print(f[N])