tc = int(input())

while tc != 0:
    tc -= 1
    given = list(map(int, input().split()))

    mean = sum(given[1:]) / given[0]
    
    cnt = 0
    for i in range(1, len(given)):
        if given[i] > mean:
            cnt += 1
    
    print("{:.3f}%".format(cnt/given[0] * 100))