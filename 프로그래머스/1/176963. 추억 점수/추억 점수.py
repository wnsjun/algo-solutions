def solution(name, yearning, photo):
    answer = []
    score={}
    
    for i in range(len(name)):
        score[name[i]]=yearning[i]
        
    for people in photo:
        sum=0
        for person in people:
            if person in score:
                sum+=score[person]
        answer.append(sum)
        
    return answer