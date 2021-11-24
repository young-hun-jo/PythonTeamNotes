# 1개~주어진 사이즈 리스트 개수별로 슬라이딩 윈도우 부분집합 구하기
sets = ['a', 'b', 'c', 'd', 'e']
n = len(sets)
for size in range(1, n+1):
    for i in range(n-size+1):
        window = sets[i:i+size]
        print(''.join(window))
