# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB

# 부분집합을 생성하고 부분집합의 합을 구하는 함수
def subset(i, ssum):
    global cnt
    if ssum > K:      # 합이 K보다 크면 더 이상 계산할 필요가 없으므로 중단한다
        return
    if i == N:        # 종료조건
        if ssum == K: # 종료시, 합이 K와 같으면 카운팅한다.
            cnt += 1
        return
    subset(i+1, ssum+arr[i])   # arr[i]를 포함하는 경우
    subset(i+1, ssum)          # arr[i]를 포함하지 않는 경우

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    subset(0, 0)

    print(f'#{t} {cnt}')