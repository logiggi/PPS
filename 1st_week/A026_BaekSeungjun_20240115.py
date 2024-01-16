def solution(x):
    answer = True
    
    strNum = str(x)
    res = 0
    for e in strNum:
        res += (ord(e) - ord('0'))
    
    answer = (x % res == 0)
    
    return answer

solution(13)