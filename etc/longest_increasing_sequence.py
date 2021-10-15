n = int(input())  # 수열의 길이
array = list(map(int, input().split()))  # 주어진 수열

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 수열 길이
res = max(dp)
print(res)
