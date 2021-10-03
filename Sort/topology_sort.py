# 선후관계를 고려한 위상 정렬 -> 진입차수, 큐 활용
from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
# 진입 차수 테이블 초기화 및 갱신
indegree = [0] * (v+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    # 진입차수가 0인 초기 노드 넣기
    queue = deque()
    result = []
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)
    # 큐가 빌 때까지 반복
    while queue:
        node = queue.popleft()
        result.append(node)
        # 인접 노드 탐색
        for next in graph[node]:
            indegree[next] -= 1
            # 새롭게 진입차수가 0이 된 노드들 큐에 넣기
            if indegree[next] == 0:
                queue.append(next)

    for i in range(len(result)):
        print(result[i], end=' ')

topology_sort()
