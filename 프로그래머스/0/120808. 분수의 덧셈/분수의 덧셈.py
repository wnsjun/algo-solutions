def solution(numer1, denom1, numer2, denom2):
    numer= denom1*numer2+denom2*numer1
    denom= denom1*denom2
    
    i=[]
    for num in range(1, min(numer,denom)+1):
        if numer%num==0 and denom%num==0:
            i.append(num)
    gn=max(i)
            
    answer = [numer/gn, denom/gn]
    return answer