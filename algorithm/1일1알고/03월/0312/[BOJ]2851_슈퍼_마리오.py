# 문제 url: https://www.acmicpc.net/problem/2851

arr = [int(input())for _ in range(10)]

total = 0         # 점수의 합을 저장할 변수
between = 100     # 점수의 합과 100의 차이를 저장할 변수

for score in arr:
    if abs(100 - (total+score)) <= between:
        between = abs(100 - (total+score))  # 절대값으로 계산
        total += score
    else:
        break

print(total)