# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD
# password 딕셔너리
# key: 암호 코드 배열을 2진수로 변환한 값
# value: 암호 코드 번호
password = {
    13: 0,
    25: 1,
    19: 2,
    61: 3,
    35: 4,
    49: 5,
    47: 6,
    59: 7,
    55: 8,
    11: 9
}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())   # N: 배열의 세로 크기 , M: 배열의 가로 크기
    arr = [input() for _ in range(N)]

    # 암호 탐색
    # 먼저 암호의 가장 끝부분 좌표를 찾는다.
    row = 0
    column = 0
    Flag = False  # 이중 for문을 나오기 위한 변수
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                row = i
                column = j
                Flag = True
                break
        if Flag:
            break

    # 7자리 숫자의 암호 코드 8개를 찾는다.
    cnt = 0
    code = []
    while cnt < 8:       # 암호코드 8개를 찾을 때 까지 반복한다.
        n = 0
        for i in range(0, 7):  # 2진수 형태의 7자리의 암호코드를 10진수로 변환한다.
            if arr[row][column-i] == '1':
                n |= 1 << i
        code.append(n)   # 10진수로 변환된 값을 저장한다.
        column -= 7      # 다음 암호코드
        cnt += 1
    code = code[::-1]    # 암호코드를 뒤에서부터 탐색했기때문에 순서를 바꿔준다.
    print(code)
    # 딕셔너리를 이용하여 암호 코드 번호로 변환.
    for i in range(0, 8):
        code[i] = password[code[i]]

    # 정상적인 암호코드인지 확인한다.
    hol = 0
    jjak = 0
    for i in range(0, 7):
        if (i+1) % 2:  # 홀수
            hol += code[i]
        else: # 짝수
            jjak += code[i]

    if not (hol*3 + jjak + code[7]) % 10:  # 정상
        print(f'#{t} {sum(code)}')
    else:                                  # 비정상
        print(f'#{t} 0')