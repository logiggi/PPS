given = input().split()

for i in range(0, len(given)):
    given[i] = int(given[i])

acnt = 0
dcnt = 0
for i in range(1, len(given)):
    if given[i-1] + 1 == given[i]:
        acnt += 1
    if given[i-1] - 1 == given[i]:
        dcnt += 1
        
if acnt == 7:
    print("ascending")
elif dcnt == 7:
    print("descending")
else:
    print("mixed")