import sys

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (n+1)
visited = [False] * (n+1)

# 간단한 다익스트라 알고리즘 구현
# 시간복잡도: O(N^2), 이 때, N=노드의 개수


def get_smallest_node():
    min_val = INF
    node = 0
    for i in range(1, n+1):
        # 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            node = i
    return node


def dijkstra(start):
    # 시작 노드 처리
    distance[start] = 0
    visited[start] = True
    for next in graph[start]:  # 시작노드의 인접노드 처리
        distance[next[0]] = next[1]
    # 시작 노드 이외의 노드들 처리
    for _ in range(n-1):
        # 방문하지 않았으면서 시작노드와 최단거리인 노드 반환
        node = get_smallest_node()
        visited[node] = True
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('X')
    else:
        print(distance[i])
