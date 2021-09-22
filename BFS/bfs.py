# BFS - 큐 사용
from collections import deque
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * len(graph)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

bfs(graph, 1, visited)
