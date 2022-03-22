# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB

# dfs로 만들 수 있는 모든 단어를 탐색한다.
def dfs(vi, vj, cnt, word):  # vi: 행, vj: 열, cnt : 단어 길이, word: 현재 만든 단어
    global result
    if cnt == 7:   # 단어가 7자리이면 단어를 set에 저장하고 리턴한다.
        result.add(word)
        return
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni = vi + di
        nj = vj + dj
        if 0 <= ni < 4 and 0<= nj <4:  # delta 범위 체크
            dfs(ni, nj, cnt+1, word+arr[ni][nj])

T = int(input())
for t in range(1, T+1):
    arr = [list(input().split())for _ in range(4)]
    result = set()   # set을 사용함으로 중복을 방지한다.

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, arr[i][j] )

    print(f'#{t} {len(result)}')