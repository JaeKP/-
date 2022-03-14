# 문제 url: https://www.acmicpc.net/problem/2628

W,H = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

row = [0]; col = [0]     # 잘라야 하는 점선의 리스트(추후, 첫번째로 잘리는 조각의 길이를 구하기 위해 미리 0을 추가한다)

for i in range(N):
    if arr[i][0]:        # row: 가로로 자르는 점선리스트
        col.append(arr[i][1])
    else:                # col: 세로로 자르는 점선리스트
        row.append(arr[i][1])
row.sort(); col.sort()   # 오름차순 정렬

# 잘려진 조각의 가로와 세로길이를 구한다. (조각이 잘린 위치 - 조각이 시작된 위치)
# 조각이 시작된 위치는 첫번째 조각이면 0이다.
# 두번째 조각부터는 이전에 잘린 위치가 조각이 시작된 위치이다.
wide = [col[i]-col[i-1] for i in range(1, len(col))]   # 가로 길이
height = [row[i]-row[i-1] for i in range(1, len(row))] # 세로 길이

wide.append(W - col[-1]); height.append(H - row[-1])   # 마지막으로 잘린곳의 길이를 추가한다.

wide.sort(); height.sort() # 가장 큰 값을 찾기 위한 오름차순 정렬
print(wide[-1]*height[-1]) # 가장 긴 길이끼리 곱한다