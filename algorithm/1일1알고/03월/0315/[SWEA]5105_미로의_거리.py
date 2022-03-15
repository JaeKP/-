# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg#
from collections import deque
T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAZE = [input()for _ in range(N)]

    # 시작지점 찾기
    for i in range(N):
        for j in range(N):
            if MAZE[i][j] == '3':
                si, sj = i, j


    # 빈q가 아니면 반복한다.
    def BFS():
        q = deque()
        visit = [[0] * N for _ in range(N)]    # 방문여부를 확인하는 2차원 배열

        # 시작점 방문 표시
        visit[si][sj] += 1
        q.append((si, sj))

        while q:
            v = q.popleft()     # 현재 도착한 지점
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # 우하좌상
                di = v[0] + i   # 주변 좌표
                dj = v[1] + j   # 주변 좌표
                # 조건) 1. 범위내에 있고 2. 방문하지 않았던 좌표이고 3. 벽이 아니라면..
                if 0 <= di < N and 0 <= dj < N and MAZE[di][dj] == '0' and visit[di][dj] == 0: # 통로
                    visit[di][dj] = visit[v[0]][v[1]] + 1
                    q.append((di, dj))
                elif 0 <= di < N and 0 <= dj < N and MAZE[di][dj] == '2'and visit[di][dj] == 0: # 도착지점
                    visit[di][dj] = visit[v[0]][v[1]] + 1
                    return visit[di][dj]-2  # 이동한 칸수를 출력! (시작지점과 도착지점을 제외하여 -2 해야 함)
        return 0    # 도착 못하면 0을 리턴

    print(f'#{t} {BFS()}')


