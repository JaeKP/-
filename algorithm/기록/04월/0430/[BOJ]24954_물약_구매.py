# 문제 url: https://www.acmicpc.net/problem/24954

# 순열
def permutation(n, pay):
    global total_cost

    # 가지치기
    # 지불해야할 금액이 현재 최솟값인 금액보다 크면 return한다.
    if pay > total_cost:
        return

    # 종료조건 (N개의 순열이면 끝)
    if n > N:
        if total_cost > pay:
            total_cost = pay
        return

    for num in range(1, N+1):
        # 순열에 들어가있는지 확인
        if not visit[num]:
            # 할인 정보를 가격에 반영한다.
            for i in range(1, N+1):
                cost[i] -= discount[num][i]

            # 최소금액은 1원이다.
            if cost[num] <= 1:
                price = 1
            else:
                price = cost[num]
            visit[num] = 1 # 순열에 포함!
            permutation(n+1, pay+price)
            visit[num] = 0  # 복구
            for j in range(1, N+1):  # 복구
                cost[j] += discount[num][j]

 # 물약의 개수
N = int(input())

# 물약 가격
cost = [0] + list(map(int, input().split()))

# 할인 정보를 기록하는 2차원 배열
discount = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    M = int(input())
    for j in range(M):
        p, d = map(int, input().split())
        discount[i][p] = d

# 순열에 포함되었는지 확인하는 리스트 (중복순열이 아니다.)
visit = [0]*(N+1)
total_cost = 0xffffff
permutation(1, 0)

print(total_cost)