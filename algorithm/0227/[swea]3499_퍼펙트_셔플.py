# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(input().split())

    shuffle = []         # 퍼펙트 셔플 결과를 저장하는 리스트
    front = []           # 카드의 앞부분만 저장하는 리스트
    back = []            # 카드의 뒷부분만 저장하는 리스트
    median = (N-1)//2    # 앞부분과 뒷부분을 나누기 위한 중간 값

    # 카드 절반을 나눠 앞부분과 뒷부분으로 나눈다.
    for i in range(0, median + 1):
        front.append(arr[i])
    for i in range(median + 1, N):
        back.append(arr[i])

    # 카드를 교대로 뽑아 새로운 덱을 만든다.
    # front 카드 갯수 == back 카드 갯수라면, 그냥 교대로 뽑아 덱을 완성한다.
    if len(front) == len(back):
        for i in range(len(back)):
            shuffle.append(front[i])
            shuffle.append(back[i])

    # 만약 front카드 갯수 > back 카드 갯수라면, front의 마지막카드를 마지막에 추가한다.
    else:
        for i in range(len(back)):
            shuffle.append(front[i])
            shuffle.append(back[i])
        shuffle.append(front[-1])

    print(f'#{t}', end = ' ')
    print(*shuffle)




