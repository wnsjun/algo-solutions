def solution(numbers):
    answer = set() #중복제거용
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer=sorted(answer)
            
    return answer