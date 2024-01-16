N = int(input())
cost = list(map(int, input().split()))
Y = 0
M = 0
for e in cost:
    Y += (int(e / 30) + 1) * 10
    M += (int(e / 60) + 1) * 15
    
if Y < M:
    print("Y {}".format(Y))
elif Y > M:
    print("M {}".format(M))
else:
    print("Y M {}".format(Y))
