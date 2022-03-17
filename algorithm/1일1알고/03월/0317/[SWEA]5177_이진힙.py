# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg#

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최소 힙 트리
    def heap(number):
        global last
        last += 1           # 현재, 트리의 마지막 정점 번호
        tree[last] = number # 사용자가 입력한 값을 트리의 마지막 정점으로 추가한다.

        child = last
        parent = last// 2
        # 최소 힙트리이기 때문에 추가된 정점의 값을 부모의 값과 비교한다.
        # 부모의 값보다 작으면 서로 자리를 교환한다.
        # 트리의 ROOT에 도달하거나 부모의 값보다 커질때까지 반복한다.
        while parent >= 1 and tree[parent] > tree[child]:
            tree[parent], tree[child] = tree[child], tree[parent]
            child = parent
            parent = child //2

    # 사용자가 입력한 숫자를 이용하여 최소 힙 만든다.
    tree= [0]*(N+1)
    last = 0
    for num in arr:
        heap(num)

    # 마지막노드의 조상노드에 저장된 값을 더한다.
    # 마지막 노드번호는 N이다. 완전이진트리이기 때문에 부모 노드 번호는 N//2이다.
    total = 0
    n = N
    while n//2 >= 1:
        total += tree[n//2]
        n = n//2

    print(f'#{t} {total}')
