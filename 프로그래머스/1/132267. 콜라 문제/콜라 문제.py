def solution(a, b, n):
    answer = 0
    
    while n >= a:
        exchange = n // a          # 교환 횟수
        new_cola = exchange * b    # 새로 받는 콜라
        remain = n % a             # 남는 병
        
        answer += new_cola
        n = new_cola + remain
        
    return answer