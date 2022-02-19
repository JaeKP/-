T = int(input())

for t in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    i = 0                            # row 인덱스 초기화
    j = 0                            # column 인덱스 초기화
    k = 0                            # 모서리를 계산하기 위한 변수
    Number = 2                       # 입력할 숫자
    snail[i][j] = 1                  # 첫 숫자 입력!

    while Number <= N*N:            # 입력해야 할 숫자를 다 입력하면 반복문은 끝난다
        while j < N-1-k  :          # 오른쪽 상단 모서리에 도착하기 전까지 반복!
            j += 1                  # 오른쪽 한 칸 이동한 뒤,
            snail[i][j] = Number    # 숫자를 입력
            Number += 1             # 숫자를 증가

        while i < N-1-k :          # 오른쪽 하단 모서리에 도착하기 전까지 반복!
            i += 1                 # 아래로 한 칸 이동한 뒤,
            snail[i][j] = Number   # 숫자를 입력
            Number += 1            # 숫자를 증가

        while j > 0 + k:           # 왼쪽 하단 모서리에 도착하기 전까지 반복!
            j -= 1                 # 왼쪽으로 한 칸 이동한 뒤,
            snail[i][j] = Number   # 숫자를 입력
            Number += 1            # 숫자를 증가

        k += 1                     # 모서리 추가
        while i > 0 + k:           # 왼쪽 상단 모서리에 도착하기 전까지 반복!
            i -= 1                 # 위로 한 칸 이동한 뒤,
            snail[i][j] = Number   # 숫자를 입력
            Number += 1            #숫자를 증가

    print(f'#{t}')
    for i in range(N):
        print(*snail[i])







