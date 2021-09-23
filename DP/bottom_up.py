# 다이나믹 프로그래밍 -> for loop 사용 -> DP 테이블 -> Bottom-Up 방식
d = [0] * 101

d[1] = 1
d[2] = 1

for i in range(3, 101):
    d[i] = d[i-1] + d[i-2]

print(d[:11])
