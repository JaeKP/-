# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT#
from heapq import heappop, heappush

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    weight = [[0xffffff]*N for _ in range(N)]  # 가중치를 기록할 리스트 (default: 아주 큰 값)
    visit = [[0]*N for _ in range(N)]          # 정점의 확정여부를 확인하는 리스트

    weight[0][0] = 0  # 출발점의 가중치는 0이다.
    q = [(0, 0, 0)]  # w, r, c

    while q:
        w, r, c = heappop(q)     # 가중치가 가장 적은 정점을 팝!
        if visit[r][c]: continue # 확정된 정점인지 확인한다.
        visit[r][c] = 1          # 확정!

        # 인접 정점을 순회한다.
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = r + di
            nj = c + dj
            # 범위 체크
            if 0 <= ni < N and 0 <= nj < N:
                # 인접정점의 높이가 더 높으면 가중치는 높이의 차이 + 1이다
                if arr[ni][nj] > arr[r][c]:
                    value = arr[ni][nj]-arr[r][c] + 1
                else: # 높이가 더 높지 않으면 가중치는 1이다.
                    value = 1
                # 계산된 가중치와 기존의 가중치를 비교해서 계산된 가중치가 더 적으면 갱신한다.
                if weight[ni][nj] <= weight[r][c] + value:
                    continue
                weight[ni][nj] = weight[r][c] + value     # 갱신!
                heappush(q, (weight[r][c]+value, ni, nj)) # 갱신 !

    print(f'#{t} {weight[N-1][N-1]}')




