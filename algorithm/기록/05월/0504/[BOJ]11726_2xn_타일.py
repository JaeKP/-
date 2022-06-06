# 문제 url: https://www.acmicpc.net/problem/11726

# 단순 재귀
# def make_square(n):
#     global cnt
#     if n == N:
#         cnt += 1
#         return
#     make_square(n+1)
#     if n <= N-2:
#         make_square(n+2)
#
# N = int(input())
# cnt = 0
# make_square(0)
# print(cnt%100007)

# memo 활용하기
def make_square(n):
    if memo[n] != -1:
        return memo[n]

    # 2x1을 고를 때와 1x2를 고를 때의 방법의 수를 더한다.
    memo[n] = make_square(n-2)%MOD + make_square(n-1)%MOD
    return memo[n]

N = int(input())
MOD = 10007
memo = [-1]*(N+2)

# 기저사례
memo[0] = 0
memo[1] = 1
memo[2] = 2

make_square(N)
print(memo[N]%MOD)

