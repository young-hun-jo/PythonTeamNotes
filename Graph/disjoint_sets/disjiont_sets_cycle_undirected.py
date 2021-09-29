# 노드, 간선 개수 입력받기
v, e = map(int ,input().split())
parent = [0] * (v+1)   # 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# find 연산 -> 경로 압축 테크닉 활용해 부모노드 재귀적 탐색
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    # a, b 각 부모노드 탐색
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cycle = False
# 주어진 간선 정보를 하나씩 확인하면서 사이클 판별 수행 -> 단, 무방향 그래프일 때만 적용 가능
for _ in range(e):
    a, b = map(int, input().split())
    # a, b 부모노드가 같으면 사이클 발생
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # a, b 부모노드가 다르면 주어진 간선 정보에 대해 union 연산 수행
    else:
	union_parent(parent, a, b)
