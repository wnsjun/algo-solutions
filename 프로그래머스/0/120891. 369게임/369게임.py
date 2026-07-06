def solution(order):
    cnt =0
    while (order):
        a=order%10 #나머지
        order=order//10 #몫
        if a==3 or a==6 or a==9 :
            cnt+=1

    return cnt