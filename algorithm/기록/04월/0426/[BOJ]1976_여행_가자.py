# 문제 url: https://www.acmicpc.net/problem/1976
from collections import  deque

# 경로에 있는 도시를 방문했는지 확인하는 함수
def check():
    for city in route:  # 경로에 있는 도시를 순회한다.
        # 경로에 있는 도시를 방문하지 않았으면 'NO'를 리턴한다.
        if not visit[city]:
            return 'NO'
    return 'YES'

# 시작점부터 이어진 모든 도시를 방문하는 함수
def bfs(s): # s: 시작점
    q = deque()
    visit[s] = 1
    q.append(s)
    while q:
        city = q.popleft()
        for node in arr[city]:
            if not visit[node]:
                q.append(node)
                visit[node] =1

N = int(input())  # 도시의 수
M = int(input())  # 경로 수

# 인접 리스트 생성
arr = [[] for _ in range(N+1)]
for i in range(N):
    array = list(map(int, input().split()))
    for j in range(N):
        if array[j]:
            arr[i+1].append(j+1)

# 여행 경로
route = list(map(int, input().split()))

# 방문을 확인하는 리스트
visit = [0] * (N + 1)
bfs(route[0])  # 갈 수 있는 도시 모두 다 방문~!

print(check()) # 여행 경로에 있는 도시도 방문했는지 확인
