def solution(array):
    count={}
    
    #1. 빈도수 세기
    for num in array:
        count[num]=count.get(num,0)+1
        
    #2. 최댓값
    max_count=max(count.values())
    
    #3. 최빈값 
    modes = [num for num, cnt in count.items() if cnt == max_count]
        
    return modes[0] if len(modes) == 1 else -1