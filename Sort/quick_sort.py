# 퀵 정렬(Quick Sort)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 1. 일반적인 구현 - 재귀함수 사용
def quick_sort(array, start, end):
    if start >= end:
        return None
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
        while start < right and array[pivot] < array[right]:
            right -= 1
        # 인덱스 어긋나면 pivot을 right로 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    # 새로운 pivot인 right 기준으로 분할해 퀵 정렬 재귀적으로 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


# 2. Pythonic 방법
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

res = quick_sort(array)
print(res)
