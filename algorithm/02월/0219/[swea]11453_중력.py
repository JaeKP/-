T = int(input())

for t in range(1,T+1):
    arr = list(map(int, input().split()))

    max_cnt = 0                              # 최대 낙차를 저장하는 변수

    for i in range(99):                      # 낙하하는 상자
        cnt = 0                              # 낙차를 저장하기 위한 변수 (i가 순회할 때 리셋 )
        for j in range(i+1, 100):            # 낙하하는 상자 뒤에 있는 상자 순회
            if arr[i] > arr[j]:              # 낙하하는 상자가 더 크면
                cnt += 1                     # 낙차 +1
        if max_cnt < cnt:                    # 최댓값을 구하기 위한 조건문
            max_cnt = cnt

    print(f'#{t} {max_cnt}')