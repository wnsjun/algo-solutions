def solution(number, limit, power):
    arr=[]
    for i in range(1,number+1):
        cnt=0
        for k in range(1,int(i**0.5)+1):  
            if i%k==0:  
                if i==k*k:
                    cnt+=1
                else:
                    cnt+=2
        if cnt<=limit:
            arr.append(cnt)
        else:
            arr.append(power)
            
    return sum(arr)