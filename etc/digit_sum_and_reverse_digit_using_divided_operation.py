# 몫/나머지 연산 활용해서 자릿수 합 구하기
n = 910

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

# 몫/나머지 연산 활용해서 자릿수 뒤집기
n = 910

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x //= 10
    return res
