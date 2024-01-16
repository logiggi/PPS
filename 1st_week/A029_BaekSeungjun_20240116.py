N = int(input())
first = int(input())

if N > 5:
    print("Love is open door")
else:
    for i in range(1, N):
        if first == 0:
            print(1)
            first = 1
        else:
            print(0)
            first = 0