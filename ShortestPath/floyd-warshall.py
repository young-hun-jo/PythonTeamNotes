# 플로이드 워셜 알고리즘 -> 모든 노드에서 모든 노드까지의 최단 거리 
# 시간복잡도 O(N^3)
INF = int(1e9)
n = int(input())
m = int(input())
# 거리 테이블 2차원 리스트로 정의
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 자기 자신의 노드 거리는 0으로 설정
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# k = 탐색 노드
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('도달 불가', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
