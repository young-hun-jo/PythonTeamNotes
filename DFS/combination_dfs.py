# n개 중 m개를 뽑아 중복을 허용하지 않고 조합을 만드는 경우
sets = ['a', 'b', 'c', 'd', 'e']
n = len(sets)
m = 2
res = [0] * m


def dfs(L, s):
    if L == m:
        for r in res:
            print(r, end=' ')
        print()
        return
    else:
        for i in range(s, n):
            res[L] = sets[i]
            dfs(L+1, i+1)


dfs(L=0, s=0)
