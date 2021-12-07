# 10진수 -> n진수로 변환
result = ''


def dfs(x, n):
    global result
    if x == 0:
        return
    else:
        dfs(x // n, n)
        result += str(x % n)


res = dfs(245, 3)
print(res)

# n진수 -> 10진수로 변환
decimal = 0
for i, val in enumerate(res):
    decimal += (3 ** i) * int(val)   # 3진수 -> 10진수로 변환

print(decimal)
