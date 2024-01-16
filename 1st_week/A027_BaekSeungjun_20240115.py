def solution(number, k):
    answer = [] 
    
    for e in number:
        if len(answer) == 0:
            answer.append(e)
            continue
        
        if k > 0:
            while answer[-1] < e:
                answer.pop()
                k -= 1
                if k <= 0 or len(answer) == 0:
                    break
                
        answer.append(e)
                
    if k > 0:
        answer = answer[:-k]  
         
    return ''.join(answer)

solution("4177252841", 4)