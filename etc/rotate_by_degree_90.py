def rotate_a_by_degree_90(a):
    n = len(a)  # 행 길이
    m = len(a[0])  # 열 길이
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


# zip, unpacking, reversed 이용한 방법
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated = [list(reversed(col)) for col in zip(*matrix)]
print(rotated)


# reverse, reversed
a = [1, 2, 3]
a.reverse()
print(a)  # [3, 2, 1]
print(reversed(a)) # iterator 이므로 리스트나 튜플로 감싸주기
print(list(reversed(a)))  # [1, 2, 3]
