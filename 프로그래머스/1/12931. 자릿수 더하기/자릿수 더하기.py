def solution(n):
    answer = 0

    while(n):
        a=n%10
        answer+=a
        n=n//10
        

    return answer