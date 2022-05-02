# 문제 url: https://www.acmicpc.net/problem/1463

# 백트래킹
# def find_count(x, cnt):
#     global min_cnt
#     if x == 1:
#         if min_cnt > cnt:
#             min_cnt = cnt
#         return
#
#     if not x % 3:
#         find_count(x//3, cnt+1)
#     if not x % 2:
#         find_count(x//2, cnt+1)
#     find_count(x-1, cnt+1)
#
#
# min_cnt = 10000000
# find_count(10, 0)
# print(min_cnt)

# 탑다운 DP
# def find_count(x):
#     if memo[x] != -1:
#         return memo[x]
#
#     if not x % 3 and not x % 2:
#         memo[x] = min(find_count(x//3)+1, find_count(x//2)+1, find_count(x-1)+1)
#     elif not x % 3 and x % 2:
#         memo[x] = min(find_count(x//3)+1, find_count(x-1)+1)
#     elif not x % 2 and x % 3:
#         memo[x] = min(find_count(x//2)+1, find_count(x-1)+1)
#     else:
#         memo[x] = find_count(x-1)+1
#     return memo[x]
#
# N = int(input())
# memo = [-1]*(N+1)
# memo[0] = 0
# memo[1] = 0
# memo[2] = 1
#
# print(find_count(N))


# 메모리 초과가 떠서 바텀업으로 수정
def find_count(n):
    # 기저사례 제외
    if n <= 2:
        return

    for x in range(3, n+1):
        if not x % 3 and not x % 2:
            memo[x] = min(memo[x//3]+1, memo[x//2]+1, memo[x-1]+1) # 이전횟수 +1 중 min
        elif not x % 3 and x % 2:
            memo[x] = min(memo[x//3]+1, memo[x-1]+1)
        elif not x % 2 and x % 3:
            memo[x] = min(memo[x//2]+1, memo[x-1]+1)
        else:
            memo[x] = memo[x-1]+1

N = int(input())

# memo[2]떄문에 N+2만큼 배열을 만든다.
memo = [-1]*(N+2)

# 기저 사례
memo[0] = 0
memo[1] = 0
memo[2] = 1

find_count(N)
print(memo[N])

