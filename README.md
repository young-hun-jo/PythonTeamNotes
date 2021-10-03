## PythonTeamNotes
- 알고리즘을 native Python으로 구현한 소스코드를 기록하는 레포지토리

### Search(탐색)
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/tree/main/DFS'>DFS(깊이우선탐색)</a>
    - 유방향 그래프에서 사이클 판별
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/tree/main/BFS'>BFS(너비우선탐색)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Search/linear_search.py'>Linear(Sequential) Search(선형탐색)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Search/binary_search.py'>Binary Search(이진탐색)</a>
    - 이진탐색을 활용해 정렬된 배열에서 특정한 원소를 찾는 방법: <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Search/bisect_count_by_range.py'>bisect 라이브러리 활용</a>
### Dynamic Programming(동적 프로그래밍)
- 메모제이션 기법(Top-Down 방식): <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DP/top_down.py'>재귀함수 활용</a>
- DP 테이블 기법(Bottom-Up 방식): <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/DP/bottom_up.py'>for loop 활용</a>
### Sort(정렬)
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/selection_sort.py'>Selection Sort(선택 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/insertion_sort.py'>Insertion Sort(삽입 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/quick_sort.py'>Quick Sort(퀵 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/counting_sort.py'>Counting Sort(계수 정렬)</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/heap_sort.py'>Heap Sort(최소/최대 힙 정렬)</a>
- 그래프 데이터를 사용하는 <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Sort/topology_sort.py'>Topology Sort(위상 정렬)</a>
### Shortest Path(최단 경로)
- 다익스트라(Dijksttra) 알고리즘
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/ShortestPath/dijkstra_simple.py'>간단한 방법</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/ShortestPath/dijkstra_heqpq.py'>우선순위 큐 활용한 방법</a>
- <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/ShortestPath/floyd-warshall.py'>플로이드-워셜(Floyid-Warshall) 알고리즘</a>
### Graph(그래프 알고리즘)
- 서로소 집합 자료구조
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Graph/disjoint_sets/disjoint_sets.py'>서로소 집합 자료구조 알고리즘</a>
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Graph/disjoint_sets/disjiont_sets_cycle_undirected.py'>무방향 그래프에서 사이클 판별</a>
- 신장트리
    - <a href='https://github.com/young-hun-jo/PythonTeamNotes/blob/main/Graph/spanning_tree/kruskal.py'>크루스칼 알고리즘</a>
        - 전체 그래프에서 최소 신장 트리 2개로 분할하는 방법: 최초의 최소 신장 트리에서 비용이 가장 큰 간선 제거하기
