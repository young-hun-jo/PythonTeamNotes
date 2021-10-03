# 투 포인터를 활용해 두 리스트의 합집합 후 정렬시키기 가능
# 단, 주어진 두 리스트는 정렬되어 있어야 함!
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 7]

i, j = 0, 0              # a, b의 index = i, j
result = [0] * (n+m)     # 두 리스트를 합집합한 길이의 리스트 초기화
k = 0    # result의 인덱스

while i < n or j < m:
    # b 리스트를 다 탐색했거나, a[i] < b[j] -> a[i]의 값을 결과에 넣고, i+1
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)
