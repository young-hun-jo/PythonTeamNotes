# 힙 정렬 -> 시간복잡도 O(NlogN)
import heapq

array = [1, 3, 5, 7, 9, 0, 2, 4, 8, 6]

# 최소 힙 정렬
def min_heap_sort(array):
    q = []
    result = []
    for i in range(len(array)):
        heapq.heappush(q, array[i])
    for i in range(len(array)):
        result.append(heapq.heappop(q))

    return result

min_res = min_heap_sort(array)
print(min_res)

# 최대 힙 정렬
def max_heap_sort(array):
    q = []
    result = []
    for i in range(len(array)):
        heapq.heappush(q, -array[i])  # 삽입 시 부호 변경
    for i in range(len(array)):
        result.append(-heapq.heappop(q))

    return result

max_res = max_heap_sort(array)
print(max_res)
