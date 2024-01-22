t = int(input())

if t % 10 != 0:
    print(-1)
else: 
    acnt = bcnt = ccnt = 0
    while t > 0:
        if t >= 300:
            t -= 300
            acnt += 1
        elif t >= 60:
            t -= 60
            bcnt += 1
        else:
            t -= 10
            ccnt += 1
            
    print(acnt, bcnt, ccnt)