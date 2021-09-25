# 개선된 다익스트라 알고리즘
# 시간복잡도 O(ElogN)
import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF] * (n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작노드->시작노드 거리 계산
    while q:
        dist, node = heapq.heappop(q)
        # 기존 거리 테이블의 값 > 큐에서 뽑아낸 거리 이면 무시
        if dist > distance[node]:
            continue
        # 큐에서 뽑아낸 노드와 연결된 노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]    
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0])) 


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('X')
    else:
        print(distance[i])
