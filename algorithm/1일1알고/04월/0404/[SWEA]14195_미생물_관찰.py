# 문제 url: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AX_Pn1I6fBQDFARi&categoryId=AX_Pn1I6fBQDFARi&categoryType=CODE
from collections import deque

# 탐색
def bfs(row, column):
    word = arr[row][column]  # 탐색할 단어를 저장한다.
    q = deque()

    # 초기 세팅
    q.append((i, j))
    visit[i][j] = 1   # 방문체크
    size = 1          # 미생물의 크기를 기록한다.
    while q:
        vi, vj = q.popleft()
        # 델타로 주변 미생물을 탐색한다.
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = vi + di
            nj = vj + dj
            # 범위체크, 방문한 적이 없는 나와 같은 미생물이라면 탐색한다.(이동)
            if 0 <= ni < N and 0 <= nj <M and not visit[ni][nj] and arr[ni][nj] == word:
                q.append((ni, nj))  # 내 친구!
                visit[ni][nj] = 1   # 내 친구!
                size += 1           # 내 친구!
    return size

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input())for _ in range(N)]
    visit = [[0]*M for _ in range(N)]

    micro = [0]  # 미생물 크기를 저장하는 리스트
    dict = {'A':0, 'B':0}
    for i in range(N):
        for j in range(M):
            # 방문한 적이 없는 미생물이면 탐색의 시작점으로 삼고 내 근처에 나와 같은 개체가 있는지 탐색한다.(bfs함수)
            if arr[i][j] != '_' and not visit[i][j]:
                dict[arr[i][j]] += 1  # 미생물 개체의 수를 딕셔너리에 기록한다.
                micro.append(bfs(i, j))

    micro.sort(reverse=True)
    print(f"#{t} {dict['A']} {dict['B']} {micro[0]}")