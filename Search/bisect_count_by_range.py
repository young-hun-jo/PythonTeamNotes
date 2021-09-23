# 정렬된 배열에서 특정한 원소를 찾아야할 때 -> 이진탐색 활용 ->  bisect 라이브러리 사용
from bisect import bisect_left, bisect_right


def count_by_range(array, left_value, right_value):
    left_idx = bisect_left(array, left_value)
    right_idx = bisect_right(array, right_value)
    print('left:', left_idx, 'right:', right_idx)
    return right_idx - left_idx


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
res = count_by_range(a, 4, 4)

res = count_by_range(a, -1, 3)
res = count_by_range(a, a[0]-1, 3)
