# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT

def energy(i, used, cost):  # i: 순열 인덱스, used: 순열에 값이 있는지 확인하기 위한 값, cost: 비용
    global min_cost
    if cost >= min_cost:    # 가지 치기
        return
    if i == N:            # 종료 조건
        if min_cost > cost:
            min_cost = cost
        return

    for product in range(0, N):
        if used & (1 << product): # i 번째 자리가 1인지 확인한다. (1이면 순열에 포함된 상태)
            continue
        energy(i+1, used|(1<<product), cost+arr[i][product]) # 순열의 i번째 값이 product인 상태로 i+1번째 값을 구하러 간다.

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    memo = [0] * 2**N
    min_cost = 99 * N  # 최솟값을 구하기 위한 변수 (default: 최댓값)

    energy(0, 0, 0)
    print(f'#{t} {min_cost}')