# 부분집합 구하기
sets = ['a', 'b', 'c', 'd', 'e']
n = len(sets)
check = [0] * n


def dfs(L):
    if L == n:
        for i in range(n):
            if check[i] == 1:
                print(sets[i], end=' ')
        print()
        return
    else:
        check[L] = 1
        dfs(L+1)
        check[L] = 0
        dfs(L+1)

dfs(0)
