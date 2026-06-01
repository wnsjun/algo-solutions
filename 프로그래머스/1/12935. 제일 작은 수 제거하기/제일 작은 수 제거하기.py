def solution(arr):
    if len(arr) == 1:
        return [-1]

    min_value = arr[0]

    for i in range(len(arr)):
        if min_value > arr[i]:
            min_value = arr[i]

    answer = []

    for i in range(len(arr)):
        if arr[i] != min_value:
            answer.append(arr[i])

    return answer