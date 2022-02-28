T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    oil_map = list(map(int, input().split()))

    # 위치 리스트 만들기
    station_list = [0]*(N+1)                    # 총 이동해야 하는 거리를 표현하는 0으로 가득 찬 빈 리스트를 생성
    for oil_station in oil_map:         
        station_list[oil_station] += 1          # 주유소가 있는 곳에 1을 더한다. 

    # 움직이기
    bus = 0                                     # 기름이 꽉 찬 버스위치에 대한 변수  
    cnt = 0                                     # 기름 충전횟수에 대한 변수 
    while bus < N - K:                  
        oil = 0                                 # 기름을 충전 상태를 확인하기 위한 변수
        for location in range(bus, bus+K+1):    # 버스가 최대로 이동할 수 있는 거리의 범위를 순회
            if station_list[location] == 1:     # 주유소가 있다면 기름을 충전
                oil = location                   
                station_list[location] -= 1     # 중복으로 주유소 카운트하는 것을 방지하기 위해 -1 
        if oil == 0:                            
            cnt = 0                             
            break
        else:
            bus = oil
            cnt += 1
    print(f'#{t} {cnt}')
























    #
    #
    # while bus < N - K:
    #     for i in range(bus + K, bus, -1):
    #         if d[i] == 1:
    #             bus = i  # 충전하기
    #             cnt += 1
    #             break
    #     else:
    #         cnt = 0
    #         break
    # print(cnt)








