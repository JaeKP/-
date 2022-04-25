# 문제 url: https://www.acmicpc.net/problem/15686

# 치킨집에서 가정집까지의 거리를 구하는 함수
def calc_distance():
    total_distance = 0 # 현재 치킨집 조합의 최종 최소 치킨 거리를 기록할 변수
    # 가정집 순회
    for i in range(len(house)):
       row, column = house[i]
       distance = 0xffffff
       # 치킨집 순회
       for j in range(M):
           chicken_row, chicken_column = comb[j]
           # 어느 치킨집이 더 가까운지 비교하기 위한 조건문
           if distance > abs(chicken_row-row) + abs(chicken_column-column):
               distance = abs(chicken_row-row) + abs(chicken_column-column)
       total_distance += distance
    return total_distance

# 치킨집을 선택하는 함수
def choice_chicken(n, r, s):  # n 개 중 r개를 고르는  조합, s: 고를 수 있는 구간의 시작 인덱스
    global chicken_distance

    # 종료 조건 (치킨집을 다 고르면 종료한다.)
    if r == 0:
       ans = calc_distance()
       # 현재 도시의 치킨 거리보다 짧으면 갱신
       if chicken_distance> ans:
           chicken_distance = ans
       return

    for i in range(s, n-r+1):
        comb[r-1] = chicken[i]     # 조합 생성!
        choice_chicken(n, r-1, i+1)


N, M = map(int, input().split()) # N: 지도의 크기 M: 최대 치킨집의 수
arr = [list(map(int, input().split()))for _ in range(N)]
chicken = []  # 치킨집의 좌표를 기록하는 리스트
house = []    # 가정집의 좌표를 기록하는 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))


comb = [0]*M  # 조합을 기록하는 리스트
chicken_distance = 0xffffff # 최솟값을 구해야하기때문에 우선 엄청 큰값을 default로 설정한다.
choice_chicken(len(chicken), M, 0)

print(chicken_distance)