import sys

N = int(sys.stdin.readline())

answer = 0
for _ in range(0, N-1):
    given = int(sys.stdin.readline())
    answer += (given - 1)
    
given = int(sys.stdin.readline())
print(answer + given)