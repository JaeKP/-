# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT#

delta = [(1, 0), (0, 1)] # 아래, 오른쪽
def find_map(row, column):
    global g_ssum
    global g_min_ssum

    if g_ssum > g_min_ssum:  # 가지 치기
        return
    if row == N-1 and column == N-1: # 도착점에 도착!
        if g_min_ssum > g_ssum:
            g_min_ssum = g_ssum
        return
    else:
        for di, dj in delta:
            ni = row + di
            nj = column + dj
            # 델타 범위체크
            if 0 <= ni < N and 0 <= nj < N:
                g_ssum += arr[ni][nj]  # 이동!
                find_map(ni, nj)
                g_ssum -= arr[ni][nj]  # 되돌아 왔다!

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    g_min_ssum = N * N * 10  # 출력해야 하는 최소 합 (default = arr배열의 값을 모두 더했을 때 가질 수 있는 최댓값)
    g_ssum = arr[0][0]       # 출발 좌표의 값을 미리 추가

    find_map(0, 0)
    print(f'#{t} {g_min_ssum}')
