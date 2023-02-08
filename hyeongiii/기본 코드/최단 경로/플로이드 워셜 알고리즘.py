"""
플로이드 워셜 알고리즘
    : 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용
- 다익스트라 알고리즘의 경우, 출발 노드가 1개이므로 다른 모든 노드까지으 ㅣ최단 거리를 저장하기 위해 1차원 리스트 사용
- 플로이드 워셜 알고리즘의 경우, 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담아야하기 때문에 2차원 리스트에 최단 거리 정보를 저장한다.
- N번의 단계에서 매번 O(N ^ 2)의 시간 소요

- DP의 종류
- 노드의 개수가 N 개라고 할 때, N 번 만큼의 단계를 반복하며 '점화식에 맞게' 2차원 리스트를 갱신하기 때문
"""

INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(1 + n)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우, 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()