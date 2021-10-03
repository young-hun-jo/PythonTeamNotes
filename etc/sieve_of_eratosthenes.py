import math

# 주어진 범위 내에서 다수의 소수 출력하는 방법 -> 에라토스테네스의 체
n, m = map(int, input().split())

# m이상 n이하 중 소수인 값들 출력하기
def count_prime_number_range(n, m):
    # 남아있는 수인지 여부 체크하는 리스트 초기화
    array = [True] * (n+1)
    # 0, 1은 소수 아님
    array[0] = False
    array[1] = False
    # 가장 작은수 i 선택해서 i의 배수들 모두 제거(단, i는 남겨놓기)
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    # True인 값들은 소수
    for i in range(2, n+1):
        if array[i]:
            print(i, end=' ')

count_prime_number_range(n, m)
