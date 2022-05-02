# 문제 url: https://www.acmicpc.net/problem/2748
def dp(x):
    # default값이 아니면 값이 기록되어있는 것이기때문에 더 이상 찾을 필요가 없다.
    if memo[x] != -1:
        return memo[x]

    # 값이 기록되지 않았다면 재귀로 찾는다.
    else:
        memo[x] = dp(x-2) + dp(x-1)
        return memo[x]

memo = [-1]*91  # default는 -1이다.

# 기저 사례
memo[0] = 0
memo[1] = 1


N = int(input())
print(dp(N))
