import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    P = []                                              # 회문을 저장하기 위한 빈 리스트

    # 회문을 확인하기 위한 함수
    def palindrome (sentence , length):
       for start in range(0, length-M+1):               # 회문 시작 지점  [0 ~ (문자열길이-회문의길이)]
           end = start + M - 1                          # 회문 도착 지점
           for rotation in range(M//2):                 # 회문의 길이//2 만큼 반복
               if sentence[start+rotation] != sentence[end-rotation]:
                   break
           else:                                        # 회문일 경우, 문자를 회문 리스트에 추가
               for word in range(start, start+M):
                   P.append(sentence[word])
       return P


    # 행 우선 순회
    for i in range(N):
        row = ''
        for j in range(N):
            row += arr[i][j]
        palindrome(row,N)

    # 열 우선 순회
    for j in range(N):
        column = ''
        for i in range(N):
            column += arr[i][j]
        palindrome(column, N)

    print(f'#{t}', end=' ')
    print(*P , sep='')
