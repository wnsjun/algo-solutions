def solution(array):
    count={}
    for num in array:
        count[num]=count.get(num,0)+1
        
    max_cnt=max(count.values())
    
    modes = [num for num, cnt in count.items() if cnt == max_cnt]
        
    return(
        modes[0] 
        if len(modes) == 1 else -1
    ) 