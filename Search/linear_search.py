# 순차 탐색(Sequential=Linear Search) - 정렬 상관 없음
array = [i for i in range(10, 30, 2)]

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i+1, target


idx, tgt = linear_search(array, 16)
print(idx, tgt)
