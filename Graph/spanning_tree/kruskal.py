# 최소신장트리를 만드는 데 비용을 찾는 크루스칼 알고리즘
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보 입력받아서 비용 순으로 오름차순 정렬
edges = []
result = 0
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
# 간선 하나씩 확인하면서 부모 노드 같지 않으면 사이클 발생 X -> 최소신장트리 포함 -> union 연산
for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)
