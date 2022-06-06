# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj

# 돌을 놓은 후 체크 할 8방향
delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, -1),(-1, 1)]

# 게임 play!
def game():
    for j, i, color in arr:
        # arr 배열의 인덱스는 0부터 시작하기 때문에 -1을 한다.
        row = i - 1
        column = j -1
        board[row][column] = color # 돌을 놓는다.
        for di, dj in delta:       # delta 범위 체크!
            path = []              # 색이 다른 돌의 위치를 기록
            for k in range(1, N):  # 거리
                ni = row + di*k
                nj = column + dj*k
                # 범위와 돌의 유무를 확인한다.
                if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 0:
                    if board[ni][nj] != color:  # 색이 다르면 기록한다.
                        path.append((ni, nj))
                    else:
                        for r, c in path:       # 색이 같으면 기록한 돌의 색을 교체
                            board[r][c] = color
                        break
                else: break # 돌이 없거나 범위를 벗어나면 이 방향에는 색을 교체할 돌이 없다.


# 바둑판의 돌 갯수를 체크 하는 함수
def check():
    global b_cnt
    global w_cnt
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] ==2 :
                w_cnt += 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split()))for _ in range(M)]  # 1은 흑돌, 2는 백돌
    board = [[0]*N for _ in range(N)]

    # 초기 셋팅
    f_row = [N//2, N//2 - 1]
    f_column = [N//2, N//2 -1]
    board[f_row[0]][f_column[0]] = 2
    board[f_row[1]][f_column[1]] = 2
    board[f_row[1]][f_column[0]] = 1
    board[f_row[0]][f_column[1]] = 1
    b_cnt = 0
    w_cnt = 0

    game()
    check()
    print(f'#{t} {b_cnt} {w_cnt} ')