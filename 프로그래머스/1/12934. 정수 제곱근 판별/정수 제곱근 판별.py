def solution(n):
    for x in range(1,int(n**0.5)+1):
        if n/x==x:
            return (x+1)*(x+1)
    return -1