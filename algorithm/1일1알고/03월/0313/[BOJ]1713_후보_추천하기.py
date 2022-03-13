# 문제 url: https://www.acmicpc.net/problem/1713

N = int(input())
S = int(input())
arr = list(map(int, input().split()))

score = [0 for _ in range(100)]      # 후보자의 득표 수를 저장할 리스트
picture = []                         # 사진 틀

for vote in arr:
    if vote in picture:              # 이미 사진틀에 게시된 경우, 득표 수 + 1
        score[vote-1] += 1
    elif len(picture) < N:           # 사진틀에 자리가 있는 경우, 사진 틀에 게시한 후 득표수 +1
        score[vote - 1] += 1
        picture.append(vote)
    else:                            # 사진틀에 자리가 없고 새로 추천 받은 경우
        min_score = 1001
        for i in range(N):           # 득표수가 가장 낮고 먼저 게시된 후보자를 찾기 위해 사진틀 인덱스를 순회 함
            if min_score > score[picture[i]-1]:
                min_score = score[picture[i]-1]
                min_num = i
        score[picture[min_num]-1] = 0  # 사진틀에 게시된 사진이 삭제될 경우 득표수는 0으로 리셋
        picture.pop(min_num)           # 사진틀에서 사진 삭제
        score[vote-1] += 1             # 새롭게 추천받은 학생의 득표수 +1
        picture.append(vote)           # 새롭게 추천받은 학생을 사진틀에 게시

picture.sort()
print(*picture)

