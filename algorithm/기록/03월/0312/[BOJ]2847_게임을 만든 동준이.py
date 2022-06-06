# 문제 url: https://www.acmicpc.net/problem/2847

N = int(input())
arr = [int(input())for _ in range(N)]

i = 0     # 원래 score로 수정할 레벨
cnt = 0   # 수정 횟수

# 현재레벨의 score과 다음레벨의 score를 비교한다.
while i < N-1:
    score = arr[i]          # 현재 score
    min_score = 20000       # score가 가질 수 있는 최댓값을 default로 설정
    check = False           # 현재 score가 다음 레벨 score보다 작으면 수정을 할 필요가 없기 때문에 구분하기 위한 변수
    for j in range(i+1, N): # 다음 레벨 score를 순회하기 위한 반복문
        if arr[j] <= score and arr[j] <= min_score:
            min_score = arr[j]
            min_index = j
            check = True
    if check:
        right_score = min_score - (min_index-i)
        cnt += score - right_score
    i += 1

print(cnt)