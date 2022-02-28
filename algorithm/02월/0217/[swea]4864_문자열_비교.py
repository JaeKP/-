import sys
sys.stdin = open('input.txt')

Test = int(input())

for t in range(1, Test+1):
    P = input()
    T = input()
    len_p = len(P)                  # 패턴의 길이
    len_t = len(T)                  # 문자열의 길이

    for i in range(len_t - len_p + 1):  # 인덱스 에러가 발생하지 않도록 문자열 인덱스 순회 범위 조절
        for j in range(len_p):          # 패턴의 인덱스 순회
            if T[i+j] != P[j]:          # 문자가 일치 하지 않으면
                break                   # 문자열의 다음 인덱스부터 조사한다
        else:                           # 문자열이 전부 일치 하면
            print(f'#{t} 1')            # 1을 출력하고
            break                       # 반복문 종료
    else:
        print(f'#{t} 0')                # 결국 문자열이 전부 일치하지 않으면 0을 출력



