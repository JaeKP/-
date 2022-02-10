for number in range(1, 11):
    T = int(input())
    list_ = list(map(int, input().split()))
    total = 0                       # 조망권 총합을 구하기위한 변수 정의

    # 건물 리스트를 순회하여 건물의 높이를 비교한다.
    for i in range(2, T-2):         # 테스트 케이스 양쪽 끝 2칸에는 건물이 없기때문에 순회할 필요가 없음
        max_i = 0                   # 비교군중 가장 큰 값을 할당하기 위해 변수 정의
        for j in [-2, -1, 1, 2]:    # 비교 군은 i-2, i-1, i+1, i+2
            if max_i < list_[i+j]:  # max_i보다 비교군의 값이 크면
                max_i = list_[i+j]  # 그 값을 변수에 재할당
        if list_[i] > max_i:        # 건물의 높이가 비교군의 최대 높이 보다 크면
            total += list_[i]-max_i # 그 차이를 조망권 총합에 추가
    print(f'#{number} {total}')