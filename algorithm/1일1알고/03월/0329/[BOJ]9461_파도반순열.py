# 문제 url: https://www.acmicpc.net/problem/9461

def triangle(n):
    global memo
    if memo[n] != -1:  # 이미 저장되어있으면 그 데이터 활용
        return memo[n]
    else:
        memo[n] = triangle(n-1) + triangle(n-5) # 점화식 ( 단, n>= 5이다.)
        return memo[n]


T = int(input())
for t in range(T):
    N = int(input())
    memo = [0, 1, 1, 1, 2] + [-1]*(N-4) # 기저 사례가 아닌 부분은 -1로 세팅한다
    print(triangle(N))