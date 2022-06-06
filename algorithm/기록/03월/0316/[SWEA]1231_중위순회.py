# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD

for t in range(1, 11):
    N = int(input())
    arr = [list(input().split())for _ in range(N)]

    # index: 정점번호 / value:알파벳으로 하는 리스트 생성
    word = [0]*(N+1)
    for factor in arr:
        index = int(factor[0])
        word[index] = factor[1]

    print(f'#{t}', end=' ')
   # 인덱스를 순회하여 출력
    def in_order(v):
        if v <= N:                 # 인덱스(정점번호)가 마지막 인덱스보다 작거나 같아야 실행
            in_order(v*2)          # 왼쪽 자식 조회
            print(word[v], end='') # 부모 출력
            in_order(v*2 + 1)      # 오른쪽 자식 조회
    in_order(1)
    print()