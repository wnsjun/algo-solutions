def solution(my_string):
    arr=my_string.lower()
    
    answer = ''.join(sorted(arr))
        
    return answer