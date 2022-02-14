import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    bus_station = [0] * 5000                # index+1 을 버스정류장 번호로 갖는 정류장 리스트 생성
    for i in range(0, N):                   
        A, B = map(int, input().split())
        for j in range(A, B+1):             # 버스가 방문하는 정류장에 +1
            bus_station[j-1] += 1
    

    # P개의 버스정류장의 번호와 bus station의 버스 정류장번호를 비교해서 값을 가져온다. 
    P = int(input())
    p_bus = []                              
    for i in range(0, P):                  
        N = int(input())                    # P의 버스정류장 번호
        p_bus += [bus_station[N-1]]         # bus station의 인덱스는 0부터 시작하기 때문에 -1 

    print(f'#{t}' , end = ' ')
    print(*p_bus)

