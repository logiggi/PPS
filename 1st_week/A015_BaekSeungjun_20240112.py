given = list(map(int, input().split()))

sum = 0
for e in given:
    sum += (e*e)

print(sum % 10)