# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]

    row = 0             # 행
    column = (N-1)//2   # 열 (수확을 시작하는 열)
    k = 1               # 한 행에서 몇 번 수확할 것인가!
    harvest = []
    while row < N:
        # 열이 밭의 중간 열보다 작으면
        if row < (N-1)//2:
            for plus in range(0, k):   # 수확 횟수 순회
                harvest.append(arr[row][column+plus])
            row += 1                   # 행 +1
            column -= 1                # 열 -1
            k += 2                     # 수확횟수 + 1
        # 열이 밭의 중간 열보다 크면
        elif row >= (N-1)//2:
            for plus in range(0, k):  # 수확 횟수 순회
                harvest.append(arr[row][column + plus])
            row += 1                  # 행 +1
            column += 1               # 열 +1
            k -= 2                    # 수확횟수 -2
    print(f'#{t} {sum(harvest)}')






