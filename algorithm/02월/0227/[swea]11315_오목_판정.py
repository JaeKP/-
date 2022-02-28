# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input())for _ in range(N)]

    # 행 우선 순회
    def check():
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'o':
                    for r, c in [(0, 1), (1, 1), (1, 0), (1, -1)]: # 가로, 우측하단 대각선, 세로, 좌측하단 대각선 좌표
                        cnt = 1                                    # 오목을 카운팅하기 위한 변수
                        row = i
                        column = j
                        while 0<= row+r < N and 0 <= column+c < N: # 오목판 범위 내로 한정함
                            row += r  # 행 이동
                            column += c  # 열 이동
                            if arr[row][column] == 'o':            # 'o'이면 카운팅
                                cnt += 1
                                if cnt == 5:                       # 오목이면, 모든 반복문을 나감
                                    return 'YES'
                            else: break                            # 'o'이 아니면 다시 찾기

        return 'NO'

    print(f'#{t} {check()}')