# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg

T = int(input())

case = [0, 1, 3]         # N=10일 때는 1개의 경우의 수 , N=20 일 때는 3개의 경우의 수를 갖고 있음을 표현한 리스트.
for i in range(3, 31):   # 10≤N≤300, N은 10의 배수이기 때문에 모든 경우의 수를 미리 구함.
    # (N-10의  경우의 수) + (N-20의 경우의 수 *2) = N의 경우의 수.
    # 이에 대한 추가적인 내용은 문제풀이 참고.
    case.append(case[-1] + case[-2]*2)

for t in range(1, T+1):
    N = int(input()) // 10   # case의 인덱스는 N//10으로 이루어져 있음
    print(f'#{t} {case[N]}')