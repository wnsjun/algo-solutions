def solution(number, limit, power):
    sum=0
    
    arr=[]
    for i in range(1,number+1): #1부터 10까지 6
        cnt=0
        for k in range(1,int(i**0.5)+1): #1부터 3
            if i%k==0: #k가 i의 약수면 
                if i==k*k: #제곱수로 약수면 
                    cnt+=1 #하나 더해
                else:
                    cnt+=2 #쌍이니까 두개 더해
        if cnt>limit:
            sum+=power
        else:
            sum+=cnt
        
    return sum