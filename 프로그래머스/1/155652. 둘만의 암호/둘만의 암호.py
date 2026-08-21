def solution(s, skip, index):
    answer = ''
    for i in s:
        cnt=0
        
        while cnt<index:
            i=chr((ord(i)-ord('a')+1)%26+ord('a'))
            
            if i not in skip:
                cnt+=1
        answer+=i
    return answer