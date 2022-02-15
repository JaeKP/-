T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_a = 1                     # A가 이진 탐색을 하는 횟수 (무조건 1번은 하기때문에 1로 설정)
    cnt_b = 1                     # B가 이진 탐색을 하는 횟수 (무조건 1번은 하기때문에 1로 설정)

    # A가 이진 탐색을 하는 횟수 계산
    s = 1                        # 시작 페이지
    p = P                        # 도착 페이지

    while (s+p)//2 != A:         # A를 찾는다면 중단
        cnt_a += 1               # 탐색 횟수 +1
        if (s+p)//2 > A:         # 만약 중간 값이 A보다 크다면
            p = (s+p)//2         # 도착 페이지를 중간 값으로 변경
        else:                    # 만약 중간 값이 A보다 작다면
            s = (s+p)//2         # 시작 페이지를 중간 값으로 변경

    # B가 이진 탐색을 하는 횟수 계산
    s = 1
    p = P
    while (s+p)//2 != B:
        cnt_b += 1
        if (s+p)//2 > B:
            p = (s+p)//2
        else:
            s = (s+p)//2

    # A와 B의 횟수를 비교
    if cnt_a < cnt_b:
        print(f'#{t} A')
    elif cnt_a > cnt_b:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')
