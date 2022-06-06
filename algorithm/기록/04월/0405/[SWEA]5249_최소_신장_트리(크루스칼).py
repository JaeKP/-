# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT#
# 크루스칼로 다시 풀어보기

# 해당 정점의 root를 찾는 함수
def find_set(node):
    # root의 parent는 자기 자신이기 때문에 parent[node] = node일 때까지 반복한다.
    while parent[node] != node:
        node = parent[node]
    return node


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [tuple(map(int, input().split()))for _ in range(E)]
    arr.sort(key=lambda x: (x[2])) # 가중치 오른차순으로 정렬한다.

    parent = [num for num in range(V+1)] # 정점의 부모
    cnt = 0                              # 간선의 개수
    total_weight = 0                     # 가중치의 합

    # 가중치가 낮은 순서로 정렬된 간선들을 순회한다.
    for u, v, w in arr:
        if cnt == V:  # 종료 조건
            break
        # 해당 정점의 root 찾기
        u_r = find_set(u)
        v_r = find_set(v)
        if u_r == v_r: continue
        # 아직 정점끼리 연결되지 않았다면,해당 간선은 확정된다.
        parent[u_r] = v_r # 확정!
        cnt += 1          # 간선 개수 + 1
        total_weight += w # 가중치+

    print(f'#{t} {total_weight}')



