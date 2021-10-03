# 투 포인터를 활용해 특정한 합을 갖는 부분 연속 수열 찾기
N = 5  # 주어진 수열 길이
M = 5  # 찾고자하는 부분 합
data = [1, 2, 3, 2, 5]

interval_sum = 0
end = 0
count = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += data[end]
        end += 1
    if interval_sum == M:
        count += 1
    # 부분합 <= M 되면 -> start를 이동시켜야 함 -> 수열의 start 인덱스에 있는 값을 빼줌으로써 이동한 것이나 마찬기지
    interval_sum -= data[start]
    
print(count)
