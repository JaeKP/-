import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    p = [0]                                                   # 회문 최대길이를 저장하는 빈리스트 (지역에서 재 할당하기 위해 리스트 내부에 저장)

    # 회문 찾기
    def palindrome (sentence):
       for p_length in range(2, 101):                         # 회문의 길이 [2 ~ 문자열 길이]
           for start in range(0, 101-p_length):               # 회문 시작 지점  [0 ~ (문자열길이-회문의길이)]
               end = start + p_length -1
               for rotation in range(p_length//2):            # 회문의 길이//2 만큼 반복
                   if sentence[start+rotation] != sentence[end-rotation]:
                       break
               else:                                          # 회문이면
                   q = []                                     # 회문을 저장할 빈 리스트
                   for word in range(start, start+p_length):
                       q.append(sentence[word])
                   if len(q) > p[0]:                          # 회문의 길이를 비교
                       p[0] = len(q)


    # 행 우선 순회
    for i in range(100):
        row = ''
        for j in range(100):
            row += arr[i][j]
        palindrome(row)

    # 열 우선 순회
    for j in range(100):
        column = ''
        for i in range(100):
            column += arr[i][j]
        palindrome(column)

    print(f'#{T} {p[0]}')
