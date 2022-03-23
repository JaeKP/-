# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq

import sys
sys.stdin = open('input.txt')

def check(i, pay, day, month, three_month):
    global min_sum
    if pay > min_sum: # 가지 치기
        return
    if i > 11:    # 종료 조건 ( 0부터 시작하기때문에 11보다 커지면 종료)
        if min_sum > pay:
            min_sum = pay
        return
    check(i+1, pay+plan[i]*day, day, month, three_month)  # 1일 이용권 구매
    check(i+1, pay+month, day, month, three_month)        # 1달 이용권 구매
    check(i+3, pay+three_month, day, month, three_month)  # 3달 이용권 구매

T = int(input())
for t in range(1, T+1):
    DAY, MONTH, THREE_MONTH, YEAR = map(int, input().split())
    plan = list(map(int, input().split()))

    min_sum = YEAR   # 1년 이용권 금액 비용을 최소 지출 비용을 디폴트로 설정한다.
    check(0, 0, DAY, MONTH, THREE_MONTH)

    print(f'#{t} {min_sum}')

