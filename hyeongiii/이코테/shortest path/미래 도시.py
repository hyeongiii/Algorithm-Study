import sys
input = sys.stdin.readline

INF = 999999999

# 노드, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 2차원 리스트를 만들고 모든 값을 INF로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 사진으로 가는 것을 0으로 초기화
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 값을 입력받아 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 최종 목적지, 경유지
x, k = map(int, input().split())

for a in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][a] + graph[a][j])

if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])


