# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg#

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1     # 정점의 개수

    left = [0]*(V+1)    # 왼쪽 자식 (이진트리)
    right = [0]*(V+1)   # 오른쪽 자식 (이진트리)

    # 자식 번호를 인덱스로 부모 번호를 저장한다.
    for i in range(0, E*2, 2):
        parent = arr[i]
        child = arr[i+1]
        # 왼쪽 자식의 자리가 비어 있으면 왼쪽 자식에 추가
        # 왼쪽 자식의 자리가 채워져있으면 오른쪽 자식에 추가
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    cnt = 0      # 정점 방문 횟수를 저장하는 변수
    # 트리를 순회한다.
    def tree(v):
        global cnt
        if v:
            cnt += 1   # 정점에 방문 => 방문 횟수를 추가
            tree(left[v])
            tree(right[v])
        return cnt

    print(f'#{t} {tree(N)}') # 트리에 방문한 정점의 횟수가 트리의 수와 같기 때문에 이를 출력한다.