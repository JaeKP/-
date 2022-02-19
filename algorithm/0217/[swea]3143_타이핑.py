#for문 사용
T = int(input())

for t in range(1, T+1):
    A, B = input().split()
    la = len(A)
    lb = len(B)
    list_A = list(A)
    cnt = 0                           # 패턴 중복횟수를 저장하기 위한 변수

    for i in range(0, la-lb+1):
        for j in range(lb):
            if list_A[i+j] != B[j]:   # 같지 않다면
                break                 # list_A의 다음 인덱스부터 다시 조사!
            else:
                list_A[i+j] = []      # 중복 검색을 막기위해 문자를 제거
        else:
            cnt += 1                  # 패턴 중복 횟수 카운팅

    print(f'#{t} {la-((lb-1)*cnt)}')

import sys
sys.stdin = open('input.txt')

#======================================================================
# while문 사용
T = int(input())

for t in range(1, T+1):
    A, B = input().split()
    la = len(A)
    lb = len(B)
    cnt = 0
    i = 0                              # 인덱스 리셋
    j = 0                              # 인덱스 리셋

    while i < la and j < lb :
        if A[i] != B[j]:
            i -= j                     # 조사하기 전으로 인덱스 리턴
            j = -1                     # j 인덱스 리셋 (나중에 +1하니까)

        if j == lb-1 and A[i] == B[j]: # 만약 패턴이 중복된다면,
            cnt += 1                   # 카운팅
            j = -1                     # j만 인덱스 리셋 (나중에 +1하니까)

        i += 1
        j += 1


    print(f'#{t} {la-((lb-1)*cnt)}')




