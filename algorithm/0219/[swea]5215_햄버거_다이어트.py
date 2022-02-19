# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=햄버거+다이어트
T = int(input())

for t in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0                       # 선호도를 비교하기 위한 변수

    # 부분집합
    for sub_set in range(1<<N):         # arr의 부분집합의 개수이자, arr의 몇번째 원소가 부분집합에 포함되었는지 확인할 수 있는 수를 순회한다.
        total = 0                       # 칼로리의 합을 저장하기 위한 변수
        score = 0                       # 선호도를 저장하기 위한 변수
        for i in range(N):              # arr 인덱스 순회
            if sub_set & (1<<i):        # sub_set의 i번째 자리가 1이라면, 부분집합에 arr[i]가 포함되어 있음을 의미
                total += arr[i][1]
                score += arr[i][0]
                if total <= L and score > max_score:  # 조건1) 칼로리의 합은 1000이하. 조건2) 선호도의 합은 max_score보다 커야 함.
                    max_score = score
    print(f'#{t} {max_score}')

