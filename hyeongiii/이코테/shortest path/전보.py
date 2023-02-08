import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

# 노드 개수, 간선 개수, 시작 위치
n, m, start = map(int, input().split())
# 노드들의 관계를 기록하는 그래프
graph = [[] for i in range(n + 1)]
# 거리를 기록하는 리스트
distance = [INF] * (n + 1)

# 노드들의 관계 표시
for _ in range(m):
    # 시작 노드, 도착 노드, 걸리는 시간
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dis, now = heapq.heappop(q)
    if distance[now] < dis:
        continue
    for i in graph[now]:
        cost = i[1] + dis
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

num = 0
d = 0

for i in distance:
    if i != INF:
        num += 1
        d = max(d, i)

print(num - 1, d)