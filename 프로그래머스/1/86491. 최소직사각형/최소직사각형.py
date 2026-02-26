def solution(sizes):
    w_max=0
    h_max=0
    
    for w,h in sizes:
        w_max=max(w_max,max(w,h))
        h_max=max(h_max,min(w,h))
        
    answer= w_max* h_max
    
    return answer