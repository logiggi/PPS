def solution(s):
    answer = True
    pcnt = ycnt = 0

    for e in s:
        if e == 'p' or e == 'P':
            pcnt += 1
        if e == 'y' or e == 'Y':
            ycnt += 1

    if pcnt != ycnt:
        answer = False

    return answer