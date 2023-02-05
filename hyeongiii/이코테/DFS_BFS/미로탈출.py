from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 이동할 네 방향 정의 : 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스 코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 방향에서 네 방향으로의 위치 확인
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표가 영역을 벗어날 경우 무시
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 해당 좌표에 괴물이 있으면 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 좌표에 처음으로 방문한 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))