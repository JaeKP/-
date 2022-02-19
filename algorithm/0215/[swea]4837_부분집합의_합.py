T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    length = len(arr)
    cnt = 0

    for subset in range(1 << length):    # 1 << length = 2**length (모든 부분 집합의 개수)
        total = 0                        # 부분 집합의 합을 계산할 변수 (매번 초기화)
        num = 0                          # 부분 집합 원소의 수를 계산하기 위한 변수 (매번 초기화)
        for n in range(length):
            if subset & (1 << n):        # 부분집합의 n번째인 수가 있는지 확인 (값이 1이면 존재)
                total += arr[n]          # 부분집합의 합에 포함
                num += 1                 # 부분집합의 원소의 수 카운트 +1

        if num == N and total == K:      # 정해진 조건과 맞다면
            cnt += 1                     # 횟수+1

    print(f'#{t} {cnt}')
