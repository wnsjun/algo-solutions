def solution(d, budget):
    d.sort()
    count = 0
    total = 0

    for money in d:
        total += money
        
        if total > budget:
            break
        count += 1

    return count