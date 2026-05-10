def solution(n, m):
    
    # 최대공약수 구하기 (유클리드 호제법)
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    g = gcd(n, m)
    l = n * m // g
    
    return [g, l]