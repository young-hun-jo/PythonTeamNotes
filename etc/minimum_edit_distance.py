# str1 -> str2로 편집할 때의 최소거리
def edit_dist(str1, str2):
    # 행의 문자열을 열의 문자열로 편집!
    n = len(str1)  # 행
    m = len(str2)  # 열

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    # 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                                #  왼쪽(삽입) , 위쪽(삭제) , 왼쪽 위 대각선(교체)
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]  # DP테이블의 가장 오른쪽 아래가 최종 편집 최소 거리

str1 = 'sunday'
str2 = 'saturday'

res = edit_dist(str1, str2)
print(res)
