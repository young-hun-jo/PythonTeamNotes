#===================================
# 제한시간 M안에 N개의 문제 중 최대 점수 얻기
#===================================
N, M = 5, 20
score = [10, 25, 15, 6, 7]
time = [5, 12, 8, 3, 4]

# 1. 풀었던 문제 또 풀 수 있는 경우(중복 허용) -> 전진하면서 DP 테이블 갱신
dp = [0] * (M+1)
for i in range(N):
    for j in range(time[i], M+1):
        dp[j] = max(dp[j], dp[j - time[i]] + score[i])
print(dp[M])


# 2. 풀었던 문제 또 풀 수 없는 경우(중복 허용 X) -> 후진하면서 DP 테이블 갱신
dp = [0] * (M+1)
for i in range(N):
    for j in range(M, time[i]-1, -1):
        dp[j] = max(dp[j], dp[j - time[i]] + score[i])
print(dp[M])
