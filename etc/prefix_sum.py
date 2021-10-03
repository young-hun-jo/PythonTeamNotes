# 구간 합 계산 -> 특정 구간의 모든 수를 합한 결과를 출력
# window 방식으로 구간 합을 미리 계산해놓고 필요할 때마다 꺼내 쓰기!(DP 처럼)
n = 5
data = [10, 20, 30, 40, 50]

prefix = [0]
sum_value = 0
for d in data:
    sum_value += d
    prefix.append(sum_value)

# [left, right] 쿼리 형태 left ~ right 구간 합은 몇인가?
left, right = 2, 4
result = prefix[right] - prefix[left-1]  # P[right] - P[left-1]
print(result)
