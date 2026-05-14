def solution(strings, n):
    keys = [(x[n], x) for x in strings]
    sorted_key = sorted(keys)
    result = [i[1] for i in sorted_key]
    return result