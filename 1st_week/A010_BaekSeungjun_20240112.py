def solution(s):
    if len(s) == 1:
        return 1
    answer = 9999
    res = ''
    
    tok = 1
    idx = 0
    cnt = 0
    while tok < len(s):
        if idx < len(s):
            if idx == 0:
                pstr = s[idx:idx+tok]
                
            if pstr == s[idx:idx+tok]:
                cnt += 1
            else:
                if cnt == 1:
                    res += pstr
                else:
                    res += pstr
                    res += str(cnt)
                cnt = 0
                pstr = s[idx:idx+tok]
                cnt += 1
            idx += tok
        else:
            res += pstr
            if cnt > 1:
                res += str(cnt)
                
            answer = min(answer, len(res))
            tok += 1
            idx = 0
            cnt = 0
            res = ''
           
    return answer