# 이진 탐색(Binary Search) - 정렬되어 있을 경우에만 사용 가능
array = [i for i in range(10, 30, 2)]

# 1. 재귀함수로 구현
def binary_search(array, target, start, end):
    if start > end:
        return '찾으려는 값 없음'
    mid = (start + end) // 2
    while start <= end:
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search(array, target, mid+1, end)
        else:
            return binary_search(array, target, start, mid-1)


idx = binary_search(array, 16, 0, len(array)-1)
print(idx)

# 2. while문으로 구현
def binary_search(array, target, start, end):
    if start > end:
        return '찾으려는 값 없음'
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


idx = binary_search(array, 16, 0, len(array)-1)
print(idx)
