# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT#
from collections import deque

def bfs(i):
    q = deque()  # 빈큐
    q.append(i)  # 시작 정점을 추가한다.
    visit[i] = 1
    while q:
        v = q.popleft()
        # 해당 정점의 인접정점을 순회한다.
        for j in arr[v]:
            # 방문하지 않았다면, 무리에 추가한다.
            if not visit[j]:
                visit[j] = 1 # 같은 팀!
                q.append(j)  # 같은 팀!

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    list_ = list(map(int, input().split()))
    arr = [[] for _ in range(N+1)]
    visit = [0]*(N+1)
    team = 0

    # 인접 리스트 생성
    for i in range(M):
        arr[list_[i*2]].append(list_[i*2+1])
        arr[list_[i*2+1]].append(list_[i*2])

    # 모든 정점을 순회한다.
    for i in range(1, N+1):
        if visit[i]:    # 방문한 정점은 이미 팀이 있다.
            continue
        if not arr[i]:  # 인접 정점이 없으면 혼자 팀이다.
            team += 1
            visit[i] = 1
            continue
        bfs(i)          # 해당 정점와 같은 팀인 정점을 탐색한다.
        team += 1

    print(f'#{t} {team}')