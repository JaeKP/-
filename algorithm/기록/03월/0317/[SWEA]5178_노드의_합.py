# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg#

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(M)]

    tree = [0]*(N+1) # 빈 트리

    # 빈 트리에 사용자가 입력한 leaf를 추가한다
    for leaf in arr:
        tree[leaf[0]] = leaf[1]

    # 마지막 정점 번호 (leaf)에서 차례대로 부모 정점의 값을 채운다.
    last = N
    # ROOT(1번 정점)는 부모가 없기때문에 2번 정점까지 반복한다.
    while last >= 2:
        child = last                 # 자식 정점
        parent = child //2           # 완전 이진 트리에서는 '부모정점번호= 자식정점번호//2'
        tree[parent] += tree[child]  # 부모정점의 값은 자식 정점의 합
        last -= 1

    print(f'#{t} {tree[L]}')
