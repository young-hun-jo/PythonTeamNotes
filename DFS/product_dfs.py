# n개 중 m개를 중복해서 뽑는 일렬로 나열하는 순열 경우의 수 탐색
sets = ['a', 'b', 'c', 'd', 'e']
n = len(sets)
m = 2
res = [0] * m


def dfs(L):
    if L == m:
        for r in res:
            print(r, end=' ')
        print()
        return
    else:
        for i in range(0, n):
            res[L] = sets[i]
            dfs(L+1)


dfs(L=0)
