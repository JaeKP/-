# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=1979

import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    # 패턴 확인을 용이하게 하기 위해 배열을 0으로 둘러쌈
    arr = [[0]*(N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(N+2)]

    # 일치해야 하는 패턴
    p = [1]*K

    # 패턴을 체크하는 함수
    counting = 0
    def check(list_):
        i = 1                                            # 배열의 인덱스. arr[0]은 항상 0이기때문에 1부터 비교시작!
        j = 0                                            # 패턴의 인덱스
        while i < N+2:
            if list_[i] != p[j]:                         # 패턴이 일치 하지 않으면,
                i -= j                                   # i는 비교전의 인덱스로 회귀.
                j = -1                                   # j는 0으로 리셋할 준비를 한다.
            if j == K-1:
                if list_[i+1] == 0 and list_[i-K] == 0:  # 패턴의 앞뒤로 0이여야 한다.
                    global counting
                    counting += 1                        # 조건이 맞으면 카운팅 +1
                    j = -1                               # 0으로 리셋할 준비
                else:
                    j = -1                               # 0으로 리셋할 준비
            i += 1
            j += 1

    # 행 우선 순회
    for r in range(N+2):                                # 행
        row = [0]*(N+2)                                 # 배열을 저장할 변수
        for c in range(N+2):                            # 열
            row[c] = arr[r][c]
        check(row)

    # 열 우선 순회
    for c in range(N+2):                                # 열
        column = [0]*(N+2)                              # 배열을 저장할 변수
        for r in range(N+2):                            # 행
            column[r] =arr[r][c]
        check(column)

    print(f'#{t} {counting}')


