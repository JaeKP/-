# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB

delta = [(-1, 0), (-1, -1), (-1, +1)]  # 위, 왼쪽위, 오른쪽위

# 내가 놓을 퀸이 주어진 조건을 만족하는 지 확인하는 함수
# 내가 놓을 좌표의 위, 왼쪽 위, 오른쪽 위에 퀸이 있으면 안된다. (퀸이 있는 곳은 1로 표시했다.)
def check(row, column):
    for k in range(0, row+1):
        if not k: # k가 0일때는 조사를 안해도 된다.
            continue
        for di, dj in delta:
            ni = row + di*k
            nj = column + dj*k
            if 0 <= nj < N:       # 범위체크
                if board[ni][nj]: # 퀸이 있네 ㅠㅠ
                    return False
    return True

def dfs(row):
    global  cnt
    if row == N: # n-1번째 열에 퀸을 놓고 n이 되는 순간 종료한다.
        cnt += 1 # 체스판에 퀸을 다 놓았기때문에 카운팅!
        return

    for c in range(N):
        # 조건을 만족하면 해당자리에 퀸을 놓고 다음 열로 이동한다.
        if check(row, c):
            board[row][c] = 1
            dfs(row+1)
            board[row][c] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)] # 체스판
    cnt = 0 # 카운팅을 위한 변수

    dfs(0)
    print(f'#{t} {cnt}')