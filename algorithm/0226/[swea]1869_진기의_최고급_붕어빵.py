# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{t}' , end = ' ' )

    make_list=[0 for _ in range(max(arr)+1)]  # 0초도 추가
    n = len(make_list)

    # 만든 붕어빵의 갯수를 적은 리스트 (인덱스는 시간)
    i = 1
    while M*i <= max(arr):
        make_list[M*i] = K
        i += 1

    # 붕어빵 리스트를 누적합으로 변경!
    for i in range(1, n):
        make_list[i] = make_list[i] + make_list[i-1]


    # 구매자들의 방문시간을 순회
    arr.sort()                       # 시간 순서대로 방문시키게 하기 위해 정렬!
    for time in arr:
        if make_list[time] <= 0 :    # 방문한 시간에 붕어빵이 없으면
            print('Impossible')      # 'Impossible'출력 후 반복문 탈출
            break
        else:                        # 방문한 시간에 붕어빵이 있으면
            for i in range(time, n): # 방문한 시간부터 마지막 방문시간까지 붕어빵을 1개씩 제거! (구매했음)
                make_list[i] -= 1
    else:
        print('Possible')




