def solution(n):
    answer = []
    
    while(n):
        a=n%10
        answer.append(a)
        n=n//10    
    return answer