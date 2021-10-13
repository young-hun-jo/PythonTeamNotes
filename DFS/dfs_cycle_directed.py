v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())  # a -> b
    graph[a].append(b)

# 방문 체크 테이블
visited = [0] * (v+1)

def cycle_dfs(node):
    if visited[node]:
        if visited[node] == -1:  # 새로 방문한 노드가 DFS 끝나기 이전에 이미 방문한 노드라면!
            return True
        return False

    visited[node] = -1  # DFS 끝나기 이전 방문한 노드 체크용
    for next in graph[node]:
        if cycle_dfs(next):
            return True

    # DFS가 끝난 노드를 의미하는 것으로 1 설정 -> 해당 노드가 연결된 사이클은 없음!
    visited[node] = 1
    return False

cycle = False
for i in range(1, v+1):
    if cycle_dfs(i):
        cycle = True

if cycle:
    print('!! 현재 그래프 데이터에서 사이클 발생')
else:
    print('현재 그래프 데이터에서 사이클 발생 X')
