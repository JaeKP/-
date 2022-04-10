# 문제 url: https://www.acmicpc.net/problem/9184

# 문제에서 제시한 재귀 함수 w(a, b, c)
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        memo[a][b][c] = 1
        return memo[a][b][c]

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if memo[a][b][c] != -1:
        return memo[a][b][c]

    if a < b and b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]

    memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[a][b][c]


# 기록을 하기위한 3차원 리스트 (-50 ~ 50까지 커버한다)
memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]

while True:
    A, B, C, = map(int, input().split())
    if A == B == C == -1:  # 세 정수가 모두 -1일 경우 마지막 입력을 의미한다.
        break

    print(f'w{A, B, C} = {w(A, B, C)}')