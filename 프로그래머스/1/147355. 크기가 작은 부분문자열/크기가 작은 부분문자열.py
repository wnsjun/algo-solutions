def solution(t, p):
    cnt = 0
    p_len=len(p)
    p_int=int(p)
    
    for i in range(0,len(t)-p_len+1):
        answer=t[i:i+p_len]
        if int(answer)<=p_int:
            cnt+=1
        
    return cnt