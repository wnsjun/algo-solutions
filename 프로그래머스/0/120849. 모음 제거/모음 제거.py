def solution(my_string):

    arr=['a','e','i','o','u']
    answer=''.join([i for i in my_string if i not in arr])
    
    return answer