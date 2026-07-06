def solution(cipher, code):
    answer = ''
    n=0
    
    for i in cipher:
        n+=1
        if n%code==0:
            answer+=i
            
    return answer