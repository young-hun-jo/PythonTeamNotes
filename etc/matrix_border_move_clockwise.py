# 배열의 테두리를 시계방향으로 한 칸씩 이동시키는 방법
arr = [[8, 9, 10], [14, 15, 16], [20, 21, 22], [26, 27, 28]]

for a in arr:
    print(a)
print('-'*50)

# 테두리 기준점 왼쪽 위 좌표, 오른쪽 아래 좌표
top, left, bottom, right = 0, 0, len(arr)-1, len(arr[0])-1

# 기준점 - 왼족 위
tmp = arr[top][left]

# 왼쪽 테두리는 위로 한 칸 이동
for x in range(top, bottom):
    arr[x][left] = arr[x+1][left]
# 아래쪽 테두리는 왼쪽으로 한 칸 이동
for y in range(left, right):
    arr[bottom][y] = arr[bottom][y+1]
# 오른쪽 테두리는 아래쪽으로 한 칸 이동
for x in range(bottom, top, -1):
    arr[x][right] = arr[x-1][right]
# 위쪽 테두리는 오른쪽으로 한 칸 이동
for y in range(right, left, -1):
    arr[top][y] = arr[top][y-1]

# 왼족 위 기준점은 오른쪽으로 한 칸 이동으로 마지막 갱신
arr[top][left+1] = tmp

for a in arr:
    print(a)
