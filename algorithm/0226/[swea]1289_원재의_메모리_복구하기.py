# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN

T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input()))       # 원래 단어 (목표)

    n = len(arr)
    word = [0 for _ in range(n)]        # 현재 단어 상태 (초기화 상태)
    cnt = 0                             # 수정횟수를 저장하기 위한 변수

    for i in range(0, n):               # 단어를 비교하기 위한 인덱스 순회
        if word[i] != arr[i]:           # 만약 현재 단어와 원래 단어가 같지 않다면
            w_n = len(word[i:n])
            word[i:n] = [arr[i]] * w_n  # 단어를 수정!
            cnt += 1                    # 수정 횟수 추가

    print(f'#{t} {cnt}')

