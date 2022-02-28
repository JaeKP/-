T =  int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0

    for subset in range(1<<N):      # 부분집합을 이진수로 표현 것을 순회 (1이면 해당 인덱스 원소포함, 0이면 원소 미포함)
        total = 0                   # 부분집합 원소들의 합을 할당시킬 변수
        for i in range(N):
            if subset & (1<<i):     # 만약 subset의 i번째 문자가 1이면 A[i]는 부분집합에 포함된다.
                total += A[i]
        if total == K:
            cnt += 1

    print(f'#{t} {cnt}')
