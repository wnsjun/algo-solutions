def solution(my_string):
    sum=0
    for i in my_string:
        if '0'<=i<='9':
            sum=sum+int(i)
    return sum