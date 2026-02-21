def solution(t, p):
    answer = 0
    p_int=int(p) #비교하게 p를 숫자로 변환
    p_len=len(p)
    
    for i in range(len(t)-p_len+1):
        text=t[i:i+p_len]
        if int(text)<=p_int:
            answer+=1
            
    return answer