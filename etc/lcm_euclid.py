# 유클리드 호제법으로 최소공배수 구하기 -> 두 수를 곱한 후 최대공약수를 나눈 몫
a, b = 315, 498


# 유클리드 호제법으로 최대공약수 구하기
def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


# 최소공배수 구하기
def lcm(x, y):
    gcd_val = gcd(x, y)
    return (x * y) // gcd_val


res = lcm(a, b)
print(res)
