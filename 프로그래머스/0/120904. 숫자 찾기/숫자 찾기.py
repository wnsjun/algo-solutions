def solution(num, k):
    num=str(num)
    k=str(k)
    
    return (num.index(k)+1) if k in num else -1