def solution(d, budget):
    cnt=0
    total=0
    d.sort()
    
    for money in d:
        total+=money
        if total>budget:
            break
        cnt+=1
        
    return cnt