## 🐍 PythonTeamNotes
- 알고리즘을 native Python으로 구현한 소스코드를 기록하는 레포지토리

### 🔍 Search(탐색)
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/tree/main/DFS'>DFS(깊이우선탐색)</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DFS/dfs_cycle_directed.py'>유방향 그래프에서 사이클 판별</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DFS/subset_dfs.py'>부분집합 구하기</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DFS/product_dfs.py'>중복순열 구하기</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DFS/permutation_dfs.py'>순열 구하기</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DFS/combination_dfs.py'>조합 구하기</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/tree/main/BFS'>BFS(너비우선탐색)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Search/linear_search.py'>Linear(Sequential) Search(선형탐색)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Search/binary_search.py'>Binary Search(이진탐색)</a>
    - 이진탐색을 활용해 정렬된 배열에서 특정한 원소를 찾는 방법: <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Search/bisect_count_by_range.py'>bisect 라이브러리 활용</a>
### 🌪 Dynamic Programming(동적 프로그래밍)
- 메모제이션 기법(Top-Down 방식): <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DP/top_down.py'>재귀함수 활용</a>
- DP 테이블 기법(Bottom-Up 방식): <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DP/bottom_up.py'>for loop 활용</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/longest_increasing_sequence.py'>가장 긴 증가하는 부분 수열 길이 찾는 LIS(Longest Increasing Sequence)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/minimum_edit_distance.py'>한 문자열에서 다른 문자열로 편집하는 최소 연산 횟수</a>
### 🗂 Sort(정렬)
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/selection_sort.py'>Selection Sort(선택 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/insertion_sort.py'>Insertion Sort(삽입 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/quick_sort.py'>Quick Sort(퀵 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/merge_sort.py'>Merge Sort(병합 정렬)/a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/counting_sort.py'>Counting Sort(계수 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/heap_sort.py'>Heap Sort(최소/최대 힙 정렬)</a>
- 그래프 데이터를 사용하는 <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/topology_sort.py'>Topology Sort(위상 정렬)</a>
### 🛣 Shortest Path(최단 경로)
- 다익스트라(Dijksttra) 알고리즘
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/ShortestPath/dijkstra_simple.py'>간단한 방법</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/ShortestPath/dijkstra_heqpq.py'>우선순위 큐 활용한 방법</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/ShortestPath/floyd-warshall.py'>플로이드-워셜(Floyid-Warshall) 알고리즘</a>
### 💡 Graph(그래프 알고리즘)
- 서로소 집합 자료구조
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Graph/disjoint_sets/disjoint_sets.py'>서로소 집합 자료구조 알고리즘</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Graph/disjoint_sets/disjiont_sets_cycle_undirected.py'>무방향 그래프에서 사이클 판별</a>
- 신장트리
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Graph/spanning_tree/kruskal.py'>크루스칼 알고리즘</a>
        - 전체 그래프에서 최소 신장 트리 2개로 분할하는 방법: 최초의 최소 신장 트리에서 비용이 가장 큰 간선 제거하기
### 🔗 Etc Algorithm(기타 알고리즘)
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/is_prime_number.py'>특정 수 소수(Prime Number) 판별 알고리즘</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/sieve_of_eratosthenes.py'>주어진 범위 내 다수의 소수 판별 알고리즘(에라토스테네스의 체)</a>
- 투 포인터(Two Pointer)
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/successive_sequence_sum_by_TwoPoint.py'>특정한 합을 갖는 부분 연속 수열 찾는 알고리즘</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/merge_sort_by_TwoPoint.py'>정렬된 두 리스트 합집합 후 정렬하는 알고리즘</a>
        - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/merge_sort.py'>병합 정렬(Merge Sort)</a>에 사용됨
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/prefix_sum.py'>구간 합</a>
    - 특정 구간의 모든 수를 합하는 알고리즘
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/rotate_by_degree_90.py'>2차원 리스트 90도 회전시키기</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/change_direction_left_right.py'>상,하,좌,우 왼쪽/오른쪽 방향으로 그 때마다 다른 방향으로 회전 가능한 알고리즘</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/distribute_law_percent.py'>나누기 연산자(%)는 분배법칙 가능</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/digit_sum_and_reverse_digit_using_divided_operation.py'>몫(//), 나누기(%) 연산 활용해 정수 자릿수 합, 뒤집기 구현</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/etc/sliding_window.py'>리스트 원소 개수 별 슬라이딩 윈도우</a>
