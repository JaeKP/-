# 문제 url: https://www.acmicpc.net/problem/12927

arr = list(input())

cnt = 0                     # 변경 횟수를 카운팅 하기 위한 변수
for i in range(len(arr)):
    if arr[i] == 'Y':       # 전구가 켜져 있으면,
        arr[i] = 'N'        # 끈다
        switch = i+1         # 스위치 번호 (인덱스는 0부터 시작이기 때문에 인덱스 +1을 해야 함)
        k = 2                # 배수 계산을 하기 위한 변수

        # 스위치의 배수 번호를 가진 전구의 상태를 모두 반전
        while k* switch -1 < len(arr): # 배열의 인덱스는 스위치 번호에 -1을 해야 함
            if arr[k*switch-1]  == 'N':
                arr[k * switch - 1] = 'Y'
            else:
                arr[k * switch - 1] = 'N'
            k += 1
        cnt += 1
    else: pass

print(cnt)