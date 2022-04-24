# 문제 url: https://www.acmicpc.net/problem/1717
import sys
input = sys.stdin.readline


# 내가 현재 속한 집합의 root를 찾는 함수 (Path Compression)
def find_set(x):
    if set_root[x] != x:
        set_root[x] = find_set(set_root[x]) # 부모의 root로 변경
    return set_root[x]

# 합 집합 (union-by-rank)
# 높이가 더 낮은 트리를 더 높은 트리 밑에 넣는다.
def union(a, b):
    root_a = find_set(a)
    root_b = find_set(b)
    if root_a != root_b:
        if rank[root_a] < rank[root_b]:
            set_root[root_a] = root_b  # a_root의 root를 root_b로 변경한다.
        else:
            set_root[root_b] = root_a  # b_root의 root를 root_a로 변경한다.

        # 만약 높이가 같다면 위에서 합친 후 높이를 +1한다.
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1

N, M = map(int, input().split())
set_root = list(range(N+1))
rank = [0]*(N+1)

for _ in range(0, M):
    calc, num_a , num_b = map(int, input().split())
    if calc:
        # root가 같으면 같은 집합에 있는 것이다.
        if find_set(num_a) == find_set(num_b):
            print('YES')
        else:
            print('NO')
    else:
        union(num_a, num_b)

