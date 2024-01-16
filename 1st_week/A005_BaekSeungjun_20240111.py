def solution(skill, skill_trees):
    answer = 0
    
    is_valid = [False for i in range(26)]
    for s in skill:
       is_valid[ord(s)-ord('A')] = True 

    for st in skill_trees:
        sidx = 0
        flag = True
        for i in range(0, len(st)):
            if is_valid[ord(st[i])-ord('A')]:
                if skill[sidx] != st[i]:
                    flag = False
                    break   
                else:
                    sidx += 1

        if flag:
            answer += 1
        
    return answer