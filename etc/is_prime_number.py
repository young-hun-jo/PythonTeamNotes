# 소수 판별하는 함수(일반적인 방법) -> 시간 복잡도 O(X)
def is_prime_number(x):
    if x == 0 or x == 1:
        return '소수 아님'
    for i in range(2, x):
        if x % i == 0:
            return '소수 아님'
    return '소수'

# 소수 판별하는 개선된 함수(시간복잡도 개선) -> 시간 복잡도 O(X^1/2)로 개선
import math


def is_prime_number(x):
    if x == 0 or x == 1:
        return '소수 아님'
    for i in range(2, int(math.sqrt(x))+1):
        if x % i ==0:
            return '소수 아님'
    return '소수'
