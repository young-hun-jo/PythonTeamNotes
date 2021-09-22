# DFS - 스택, 재귀함수 사용
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

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            dfs(graph, next, visited)

dfs(graph, 1, visited)
