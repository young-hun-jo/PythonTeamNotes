# 노드, 간선 개수 입력받기
v, e = map(int ,input().split())
parent = [0] * (v+1)   # 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# find 연산 -> 선형적으로 부모노드 재귀적 탐색
def linear_find_parent(parent, x):
    if parent[x] != x:
        return linear_find_parent(parent, parent[x])
    return x

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


# 주어진 간선 정보 입력 받아서 Union-find 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


# 주어진 간선 정보들을 모두 입력 받은 뒤 노드를 하나씩 돌면서 재귀적으로 find 연산 수행해서 각 를노드 루트노드 탐색
for i in range(1, v+1):
    root = find_parent(parent, i)
    print(root, end=' ')

print()

# find 연산을 수행해 재귀적으로 수행 -> 주의)만약 find 연산이 선형적 탐색으로 구현되어 있다면 부모테이블은 직계 부모 노드값만 담겨져 출력됨!
for i in range(1, v+1):
    print(parent[i], end=' ')
