# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

# 시너지를 계산 하는 함수
def synergy(list_a, list_b):
    sum_a = 0  # 음식 a의 시너지를 저장
    sum_b = 0  # 음식 b의 시너지를 저장
    for row_a in list_a:  # 음식 a의 재료를 순회한다.
        for column_a in list_a:
            sum_a += arr[row_a][column_a]
    for row_b in list_b:  # 음식 b의 재료를 순회한다.
        for column_b in list_b:
            sum_b += arr[row_b][column_b]
    return sum_a, sum_b

# 두 요리의 시너지 차이가 최솟값인지 확인하는 함수
def min_gap_check(sum_a, sum_b):
    global min_gap
    gap = abs(sum_a-sum_b)
    if min_gap > gap:
        min_gap = gap

# 재료에 대한 부분집합을 생성하는 함수
def dfs(i,a, b):
    if i == N:  # 종료 조건 ( 재료가 0번부터 N-1번까지 있기 때문이다.)
        if len(a) == N/2 and len(b) == N/2: # 요리의 재료의 개수는 N/2여야 한다.
            sum_a, sum_b = synergy(a, b)    # 시너지 계산
            min_gap_check(sum_a, sum_b)     # 최솟값 체크
        return
    dfs(i+1, a+[i], b)    # 재료를 a 요리에 추가
    dfs(i+1, a, b+[i])    # 재료를 b 요리에 추가

    if len(a) > N/2 or len(b) > N/2:  # 요리의 재료의 개수는 N/2여야 한다.
        return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    food_a = []   # 요리 a의 재료를 저장
    food_b = []   # 요리 b의 재료를 저장
    min_gap = 20000   # 최대 시너지가 20000이기때문에 최솟값의 default로 설정
    dfs(0,food_a,food_b)

    print(f'#{t} {min_gap}')