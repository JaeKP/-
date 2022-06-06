# 문제 url: https://www.acmicpc.net/problem/1904

# dfs
# def dfs(n):
#     global  cnt
#     if n <= 0 :
#         cnt += 1
#         return
#     if n >= 2:
#         dfs(n-2) # 00 선택
#         dfs(n-1) # 1 선택
#     else:
#         dfs(n-1)
#
# N = int(input())
# cnt = 0
# dfs(N)
#
# print(cnt)

# 탑 다운
# def dp(n):
#     if memo[n] != -1:
#         return memo[n]
#     memo[n] = (dp(n-2) + dp(n-1)) % 15746
#     return memo[n]
#
# # n일때, 만들 수 있는수열의 개수를 기록하는 리스트
# memo = [-1]*1000001 # 0부터 1,000,000까지!
#
# # 기저 사례 (가장 작은 문제)
# memo[1] = 1 # 수열 1만 가능하기 때문에 수열의 개수는 1개
# memo[2] = 2 # 수열 1, 00이 가능하기 때문에 수열의 개수는 2개
#
# N = int(input())
# print(dp(N))


# 숫자가 클 때는 바텀 업 방식으로 풀자
def dp(n):
    if memo[n] != -1:
        return memo[n]
    for i in range(3, n+1):
        memo[i] = (memo[i-2] + memo[i-1]) % 15746
    return memo[n]

# n일때, 만들 수 있는수열의 개수를 기록하는 리스트
memo = [-1]*1000001 # 0부터 1,000,000까지!

# 기저 사례 (가장 작은 문제)
memo[0] = 0
memo[1] = 1 # 수열 1만 가능하기 때문에 수열의 개수는 1개
memo[2] = 2 # 수열 1, 00이 가능하기 때문에 수열의 개수는 2개

N = int(input())
print(dp(N))