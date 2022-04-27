# 문제 url: https://www.acmicpc.net/problem/16562
import sys
input = sys.stdin.readline

# 루트를 찾는 함수
def find_set(x):
    if x != root[x]:
        root[x] = find_set(root[x])
    return root[x]


# 합집합
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # root_y의 친구비가 더 적다면 root_y 밑으로 root_x가 들어간다.(합집합)
    if cost[root_x] > cost[root_y]:
        root[root_x] = root_y

    # root_x의 친구비가 더 적다면 root_x 밑으로 root_y가 들어간다.(합집합)
    else:
        root[root_y] = root_x

N, M, K = map(int, input().split())  # N: 학생 수, M: 친구 관계수, K: 가지고 있는 돈

cost = [0]+list(map(int, input().split()))   # 각각 학생이 원하는 친구 비
root = list(range(N+1))                      # root를 기록하는 리스트

# 합 집합 (친구비가 더 낮은 친구가 root가 된다)
for _ in range(M):
   p1, p2 = map(int, input().split())
   union(p1, p2)

# 합집합이 끝난 후, 리스트를 루트로 정리
for r in root:
    find_set(r)

# root인 사람들에게만 친구비를 주면 된다.
money = 0   # 지출 비용
for i in range(N+1):
    if i == root[i]:
        money += cost[i]

    # 예산을 초과하면 Oh no를 출력한다.
    if money > K:
        print('Oh no')
        break
else:
    print(money)