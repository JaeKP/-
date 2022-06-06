# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu

# 조합 생성 (조건에 맞고, 가장 이득인 조합을 짠다)
def gain():
   i, j_s, j_e = honey[0]  # 첫 번째 벌통들 위치 정보 (i: 열, j_s: 벌통 시작행, j_e:마지막 벌통행)
   c, r_s, r_e = honey[1]  # 두 번째 벌통들 위치 정보 (c: 열, r_s: 벌통 시작행, r_e:마지막 벌통행)
   subset= []              # 벌통들에 있는 꿀의 양을 저장할 리스트 (추후 부분집합으로 효율을 계산한다)
   for k in range(j_s, j_e+1): # 첫 번째 벌통 순회
       subset.append(arr[i][k])
   for k in range(r_s, r_e+1): # 두 번째 벌통 순회
       subset.append(arr[c][k])
   dfs(0, 0, 0, 0, subset)  # 벌통의 이득을 계산 하는 함수


# 채취할 수 있는 벌통을 모두 탐색한다.
# 조건에 맞으면서 가장 이득인 조합을 찾는다.
def dfs(index, ssum_a, ssum_b, profit, subset):
    global ans
    # 각 벌통들이 채취할 수 있는 한계를 넘으면 안된다.
    if ssum_a > C or ssum_b > C:
        return

    # 종료 조건
    if index == len(subset):
        if ans < profit: # 수익을 비교한다.
            ans = profit
        return

    if index < M: # 첫번째 벌통들
        dfs(index+1, ssum_a+subset[index], ssum_b, profit+subset[index]*subset[index], subset) # 채취
        dfs(index+1, ssum_a, ssum_b, profit, subset)  #채취하지 않는다.

    elif index >= M: # 두번째 벌통들
        dfs(index+1, ssum_a, ssum_b+subset[index], profit+subset[index]*subset[index], subset) # 채취
        dfs(index + 1, ssum_a, ssum_b, profit, subset) # 채취하지 않는다.



# 완전탐색 (벌통 선택)
def choice():
    # 첫 번째 벌통들을 선택한다.
    for i in range(N):
        for j in range(N):
            if j+(M-1) < N:
                honey.append((i, j, j+(M-1))) # i: 행 , j: 벌통들 시작 좌표, j+(M-1): 벌통 마지막 좌표
                # 두 번째 벌통들을 선택한다.
                for r in range(N):
                    if r == i: # 첫 번째 벌통들과 같은 행인 경우,
                        for c in range(j+M, N):
                            if c+(M-1) < N:
                                honey.append((r, c, c+(M-1)))
                                gain()
                                honey.pop() # 해당 벌통들에 대해 최대 수익을 계산을 했으면 다시 제거한다.
                    else:
                        for c in range(N):
                            if c+(M-1) < N:
                                honey.append((r, c, c+(M-1)))
                                gain()
                                honey.pop()
                honey.pop()


T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split()) # N: 벌통들의 크기, M: 선택할 수 있는 벌통의 개수, C: 꿀을 채취할 수 있는 최대 양
    arr = [list(map(int, input().split()))for _ in range(N)]
    honey = [] # 벌통들을 기록하는 변수
    ans = 0    # 최대 수익을 기록하는 변수
    choice()
    print(f'#{t} {ans}')