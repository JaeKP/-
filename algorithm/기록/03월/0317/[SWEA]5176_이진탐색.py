# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg#

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # 정점의 값을 리스트에 순서대로 저장한다.
    value = []
    for num in range(1, N+1):
        value.append(num)

    # 후위 우선탐색을 통해 트리의 정점 번호의 순서를 찾는다.
    key = []
    def tree(v):
        if v > N:
            return
        tree(v*2)
        key.append(v)
        tree(v*2+1)
    tree(1)

    # 딕셔너리를 생성 (key: 정점 번호 / value: value의 숫자)
    tree_dict = {}
    for i in range(N):
        tree_dict[key[i]] = value[i]

    print(f'#{t} {tree_dict.get(1)} {tree_dict.get(N//2)}')