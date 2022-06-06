import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    # 죽은 파리의 개수를 구하는 함수
    def fly(row, column):
        die = 0
        for i in range(M):
            for j in range(M):
                die += arr[row+i][column+j]
        return die

    # 행 우선 순회
    max_total = 0
    for i in range(0, N-M+1):       # 열 순회.(N-M+1: 파리채를 고려하여 순회할 수 있는 범위)
        for j in range(0, N-M+1):   # 행 우선 순회
            total = fly(i, j)       # 죽은 파리의 개수를 total에 저장
            if max_total < total:   # total에 저장된 값이 최댓값 보다 크면
                max_total = total   # 변수 재할당

    print(f'#{t} {max_total}')









