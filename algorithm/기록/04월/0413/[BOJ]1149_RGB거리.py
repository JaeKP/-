# 문제 url: https://www.acmicpc.net/problem/1149
import sys
sys.setrecursionlimit(10000)

# dfs => 시간 초과
# def dfs(num, ssum, pre):
#     global max_ssum
#
#     if ssum >= max_ssum: # 가지 치기
#         return
#     if num == N:         # 종료 조건
#         max_ssum = min(max_ssum, ssum)
#         return
#
#     for i in range(3):  # 색을 순회
#         #이전 집의 색과 같으면 안된다.
#         if i == pre:
#             continue
#         dfs(num+1, ssum+arr[num][i], i)
#
#
# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
# max_ssum = 1000*N
# dfs(0, 0, 10)
#
# print(max_ssum)


# memo 적용하기
def recur(num, pre):

    # 종료 조건
    if num == N:
        return 0

    # 만약 default값이 아니면 저장된 최소 합이 있기 때문에 그것을 반환한다.
    if memo[num][pre] != 0xffffff:
        return memo[num][pre]

    for i in range(3):  # 색을 순회
        # 이전 집의 색과 같으면 안된다.
        if i == pre:
            continue
        # 최소 합을 memo에 저장한다.
        memo[num][pre] = min(memo[num][pre], recur(num+1, i) + arr[num][i])
    return memo[num][pre]


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
memo = [[0xffffff]*4 for _ in range(N)]

# 첫번째 집은 이전 집의 색이 없기 때문에 이전 집은 0~2이외의 집색을 선택한다고 치고 시작한다.
print(recur(0, 3))
