T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, 11, 2):    # 정렬을 10번만 해도 되기때문에 최댓값, 최솟값 정렬을 5번 반복한다.
        # 최댓값 정렬
        for n in range(i, N):
            if arr[i] < arr[n]:
                arr[i], arr[n] = arr[n], arr[i]       # 최댓값은 0,3,5,7,9에 저장하기 때문에 i와 위치 변경

        # 최솟값 정렬
        for n in range(i+1, N):
            if arr[i+1] > arr[n]:
                arr[i+1], arr[n] = arr[n], arr[i+1]   # 최솟값은 1,4,6,8,10에 저장하기 때문에 i+1와 위치 변경

    # 출력
    print(f'#{t} ', end = '')
    for i in range(10):
        print(arr[i], end = ' ')
    print()


