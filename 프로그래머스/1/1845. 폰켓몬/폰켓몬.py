def solution(nums):
    arr=[]
    cnt=0
    
    for i in range(len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
            cnt+=1
                
        if cnt==len(nums)//2:
            return cnt

    return cnt