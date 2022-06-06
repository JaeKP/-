# 메모이제이션
memo = [0 for i in range(1000001)]
memo[1] = 1  # 기저 사례
memo[2] = 2  # 기저 사례
memo[3] = 4  # 기저 사례

def dp(i):
    for index in range(4, i+1):
        memo[index] = (memo[index-1]+memo[index-2]+memo[index-3]) % 1000000009
    return memo[i]

T = int(input())
for t in range(T):
    N = int(input())
    print(dp(N))
