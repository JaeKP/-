# 문제 url: https://www.acmicpc.net/problem/2579

# def climb_stair(stair, score, cnt):
#     global max_score
#     if stair == N:
#         if score > max_score:
#             max_score = score
#         return
#     if stair < 3:
#         climb_stair(stair + 1, score + stair_score[stair + 1], cnt+1)
#     else:
#         if cnt == 0:
#             climb_stair(stair+1, score+stair_score[stair+1], cnt+1)
#     if not stair+2 > N:
#         climb_stair(stair+2, score+stair_score[stair+2], 0)
#
#
# N = int(input())
# stair_score = [0]
# for _ in range(N):
#     stair_score.append(int(input()))
# max_score = 0
# climb_stair(1, stair_score[1], 0)
# print(max_score)
#
# dp로 수정하기
def climb_stair():
    memo[1] = stair_score[1]
    if N == 1: return
    memo[2] = memo[1] + stair_score[2]
    if N == 2 : return
    memo[3] = max(stair_score[1] + stair_score[3], stair_score[2] + stair_score[3])
    if N == 3 : return

    for i in range(4, N+1):
        memo[i] = max(memo[i-2]+stair_score[i], memo[i-3]+stair_score[i-1]+stair_score[i])

N = int(input())
stair_score = [0]
for _ in range(N):
    stair_score.append(int(input()))
memo = [-1]*(N+1)

climb_stair()
print(memo[N])