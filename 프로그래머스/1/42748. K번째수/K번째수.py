def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sliced = array[i-1:j]   # i~j 자르기
        sliced.sort()           # 정렬
        answer.append(sliced[k-1])  # k번째 값 추가
    
    return answer