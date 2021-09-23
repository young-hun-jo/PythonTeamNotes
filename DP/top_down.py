# 다이나믹 프로그래밍 -> 재귀함수 사용 -> 메모제이션 활용 -> Top-Down 방식
d = [0] * 101


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(10)
print(d[:11])
