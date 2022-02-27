# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq

T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split()))for _ in range(9)]
    print(f'#{t}', end = ' ')

    flag = False
    # 행 우선 순회
    for i in range(0, 9):
        # 겹치는 수가 있는지 체크 하기위한 딕셔너리(검색하는 숫자를 키로 한다)
        counting = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for j in range(0, 9):
            if counting[arr[i][j]] == 0:      # 순회하는 숫자를 키로 하는 dictionary를 탐색하여 중복 여부를 확인
                counting[arr[i][j]] += 1      # 추후 중복의 여부를 확인하기 위해 dictionary 값에 1을 추가
            else:
                print(0)
                flag = True
                break
        if flag:
            break
    if flag:
        continue

     # 열 우선 순회
    for j in range(0, 9):
        counting = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for i in range(0, 9):
            if counting[arr[i][j]] == 0:
                counting[arr[i][j]] += 1
            else:
                print(0)
                flag = True
                break
        if flag:
            break
    if flag:
        continue


    # 델타
    start = [(0, 0),(0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]   # 시작점(3X3의 왼쪽 상단 좌표
    delta = [(0, 0), (0,1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]   # 이동 좌표(3X3을 전부 순회하기 위함)

    for i, j in start:
        counting = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for r, c in delta:
            if counting[arr[i+r][j+c]] == 0:
                counting[arr[i+r][j+c]] += 1
            else:
                print(0)
                flag = True
                break
        if flag:
            break
    if flag:
        continue

    print(1)

